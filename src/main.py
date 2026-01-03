from .wrappers.tg import get_channels_from_folder

from .factory import SourceCollection
from .core.appdata import create_global_instance
from .poster import make_new_posts_indefinitely


def main():

    appdata = create_global_instance()

    sources = SourceCollection(appdata.last_index)

    for chn_id in get_channels_from_folder():
        sources.add_channel(chn_id, do_not_name=True)

    make_new_posts_indefinitely(sources=sources)


if __name__ == "__main__":
    main()
