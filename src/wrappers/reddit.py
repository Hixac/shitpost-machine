from typing import Any
from pathlib import Path
from datetime import datetime

import praw
import requests

from ..core.exceptions import PostNotFound
from ..core.config import settings
from ..core.utility import simple_save


_session = praw.Reddit(
    client_id=settings.RED_CLIENT_ID,
    client_secret=settings.RED_CLIENT_SECRET,
    user_agent=settings.RED_USER_AGENT
)


def _get_session():
    return _session


class Subreddit:
    @property
    def name(self) -> str:
        return self._name

    def __init__(self, identifier: str):
        self._name: str = identifier
        self._date: datetime | None = None

    def get_date_of_last_post(self) -> datetime | None:
        return self._date

    def get_newest_post(self) -> Path:
        subreddit = _get_session().subreddit(self._name)
        posts = subreddit.hot(limit=10)

        for post in posts:
            if post.over_18:
                continue

            self._date = datetime.fromtimestamp(post.created_utc)
            return self._download_image(post.url)

        raise PostNotFound("Can't find any post in REDDIT dawg.")

    def _download_image(self, url: str) -> Path:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        return simple_save(response.content)

    def to_dict(self) -> dict[str, dict[str, Any]]:
        return { self.name: {} }
