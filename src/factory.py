from typing import Any
from collections.abc import Generator

from .wrappers.reddit import Subreddit
from .wrappers.tg import Channel


class SourceCollection:
    def __init__(self, last_index: int = 0):
        self._sources: list[Subreddit | Channel] = []
        self._step: int = last_index

    def iter_posts_indefinitely(self) -> Generator[Subreddit | Channel, None, None]:
        while True:
            yield self._sources[self._step % len(self._sources)]
            self._step += 1

    def add_subreddit(self, name: str):
        self._sources.append(Subreddit(name))

    def add_channel(self, name: str | int, do_not_name: bool = False):
        self._sources.append(Channel(name, do_not_name))

    def to_dict(self) -> dict[str, dict[str, Any]]:
        d: dict[str, dict[str, Any]] = {}

        for source in self._sources:
            d |= source.to_dict()

        return d
