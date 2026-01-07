from datetime import datetime

from .factory import SourceCollection
from .wrappers.vk import wall_post, upload_photo
from .core.appdata import get_appdata
from .core.utility import pause
from .core.logger import logging  # pyright: ignore


LOGGER = logging.getLogger(__file__)


ONE_HOUR = 60 * 60


def wait_for_hour():
    ser_time = get_appdata().last_serialization_time
    if ser_time is not None:
        difference = datetime.now() - ser_time
        wait_time_seconds = ONE_HOUR - difference.total_seconds()
        pause(wait_time_seconds if wait_time_seconds > 0 else 0)


def make_new_posts_indefinitely(sources: SourceCollection):
    for source in sources.iter_posts_indefinitely():

        wait_for_hour()

        try:
            path = source.get_newest_post()
        except Exception as e:
            LOGGER.exception(f"Failed while getting newest post with error: {e}")
            continue

        date = source.get_date_of_last_post()
        if date is not None and get_appdata().is_this_meme_been(date):
            continue

        try:
            photo = upload_photo(str(path))
            wall_post(msg="", attachments=photo)
        except Exception as e:
            LOGGER.exception(f"Failed while using VK api with error: {e}")
            continue

        get_appdata().add_memes(one=date)

        LOGGER.info("Successfully posted!")
