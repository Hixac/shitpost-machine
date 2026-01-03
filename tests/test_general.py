from src.factory import SourceCollection


def test_ok():
    assert True


def test_source_collection():
    sources = SourceCollection()

    sources.add_subreddit("r/whooosh")
    sources.add_subreddit("r/funny")
    sources.add_subreddit("r/asia_irl")

    sources.add_channel(123123123, do_not_name=True)
    sources.add_channel("hehe")
    sources.add_channel("lool")

    d = sources.to_dict()

    assert len(d) == 6
