from .wrappers.tg import get_channels_from_folder
from .factory import SourceCollection
from .core.appdata import create_global_instance
from .poster import make_new_posts_indefinitely


def main():

    create_global_instance()

    sources = SourceCollection()

    sources.add_subreddit("AzumangaPosting", priority=4)
    sources.add_subreddit("chiikawa_", priority=4)
    sources.add_subreddit("Asia_irl", priority=3)
    sources.add_subreddit("twittermoment", priority=3)
    sources.add_subreddit("WojakCompass", priority=3)

    for chn_id in get_channels_from_folder():
        sources.add_channel(chn_id, do_not_name=True)

    make_new_posts_indefinitely(sources=sources)


if __name__ == "__main__":
    main()
