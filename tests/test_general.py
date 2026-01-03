from src.core.exceptions import PostNotFound
from src.factory import SourceCollection
from src.wrappers.tg import Channel
from src.wrappers.reddit import Subreddit


def test_ok():
    assert True


def test_get_source(sources: SourceCollection):
    from collections import Counter

    probs = [sources.get_source().name for _ in range(1000)]
    counts = Counter(probs)

    assert counts.most_common(1)[0][0] == "sub1"


def test_get_post():
    sub = Subreddit("AzumangaPosting")

    try:
        _ = sub.get_newest_post()
    except PostNotFound as e:
        assert True
    except Exception as e:
        assert False

    chn = Channel("beobanka")

    try:
        _ = chn.get_newest_post()
    except PostNotFound as e:
        assert True
    except Exception as e:
        assert False


def test_source_collection(sources: SourceCollection):
    assert len(sources.to_dict().keys()) == 8
