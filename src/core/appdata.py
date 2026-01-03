import os
from typing import Any
from datetime import datetime

from pydantic import BaseModel, Field, field_serializer

from .config import settings


FULL_FILENAME = settings.WHERE_TO_SAVE_FILES / "appdata.json"


class _AppInformation(BaseModel):
    serialization_time: datetime | None = Field(description="Tracks serializations of model")
    last_index: int
    posted_memes: list[datetime]

    @field_serializer("serialization_time")
    def serialize_time(self, _value: datetime, _info: Any):
        """ Returns time when serialization happens and then this value saved into serialization_time field """
        return datetime.now().isoformat()


class AppInformation:

    @property
    def last_serialization_time(self) -> datetime | None:
        return self._appdata.serialization_time

    @property
    def last_index(self) -> int:
        return self._appdata.last_index

    def __init__(
        self,
        posted_memes: list[datetime] | None = None
    ):
        self._appdata: _AppInformation

        if os.path.isfile(FULL_FILENAME):
            self._appdata = self._load()
            return

        if posted_memes is None:
            posted_memes = []
        self._appdata = _AppInformation(serialization_time=None, last_index=0, posted_memes=posted_memes)

    def _save(self):
        self._appdata.serialization_time = datetime.now()
        with open(FULL_FILENAME, "w") as f:
            _ = f.write(self._appdata.model_dump_json(indent=4))
 
    def _load(self) -> _AppInformation:
        with open(FULL_FILENAME, "r") as f:
            return _AppInformation.model_validate_json(f.read())

    def is_this_meme_been(self, one: datetime) -> bool:
        return one in self._appdata.posted_memes

    def inc_index(self):
        self._appdata.last_index += 1

        self._save()

    def add_memes(
        self,
        one: datetime | None = None, 
        couple: list[datetime] | None = None
    ) -> None:
        if one is not None:
            self._appdata.posted_memes.append(one)
        if couple is not None:
            self._appdata.posted_memes.extend(couple)

        if one is None and couple is None:
            raise Exception("Empty call.")

        self._save()


_appdata: AppInformation | None = None


def create_global_instance():
    global _appdata

    if _appdata is None:
        _appdata = AppInformation()
    else:
        raise Exception("Appdata already created!")

    return _appdata


def get_appdata():
    global _appdata

    if _appdata is None:
        raise Exception("Non-initialized global variable, \
                        you need to create using create_global_instance function.")
    return _appdata
