import pytest
from typing import Any
from collections.abc import Generator

from src.factory import SourceCollection


@pytest.fixture(scope="session")
def sources() -> Generator[SourceCollection, Any, None]:
    sources = SourceCollection()

    sources.add_subreddit("sub1", priority=3)
    sources.add_subreddit("sub2")
    sources.add_subreddit("sub3")
    sources.add_subreddit("sub4")

    sources.add_channel("chn1")
    sources.add_channel("chn2")
    sources.add_channel("chn3")
    sources.add_channel("chn4")

    yield sources
