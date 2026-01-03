from datetime import datetime

import vk_api

from ..core.config import settings


USER_TOKEN = settings.USER_TOKEN
GROUP_ID = settings.GROUP_ID
WEEK_IN_SECONDS = 60 * 60 * 24 * 7


_session = vk_api.VkApi(token=USER_TOKEN)


def _get_session() -> vk_api.VkApi:
    return _session


def wall_post(msg: str, attachments: str) -> None:
    _get_session().method("wall.post", {"owner_id": GROUP_ID, "message": msg, "attachments": attachments, \
                   "publish_date": datetime.now().timestamp() + WEEK_IN_SECONDS})


def upload_photo(direc: str | list[str]) -> str:
    upload = vk_api.VkUpload(_get_session())
    temp = upload.photo_wall(direc, group_id=-GROUP_ID)

    ret: list[str] = []
    for photo in temp:
        ret.append("photo" + str(photo["owner_id"]) + "_" + str(photo["id"]))

    return ",".join(ret)
