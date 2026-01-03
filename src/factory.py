from typing import Any
from collections.abc import Generator
from random import choices

from .wrappers.reddit import Subreddit
from .wrappers.tg import Channel


class SourceCollection:
    def __init__(self, last_index: int = 0):
        self._sources: list[Subreddit | Channel] = []
        self._priorities: list[int] = []

    def iter_posts_indefinitely(self) -> Generator[Subreddit | Channel, None, None]:
        while True:
            yield self.get_source()

    def get_source(self) -> Subreddit | Channel:
        return choices(self._sources, weights=self._priorities, k=1)[0]

    def add_subreddit(self, name: str, priority: int = 1):
        self._sources.append(Subreddit(name))
        self._priorities.append(priority)

    def add_channel(self, name: str | int, do_not_name: bool = False, priority: int = 1):
        self._sources.append(Channel(name, do_not_name=do_not_name))
        self._priorities.append(priority)

    def to_dict(self) -> dict[str, dict[str, Any]]:
        d: dict[str, dict[str, Any]] = {}

        for source in self._sources:
            d |= source.to_dict()

        return d
