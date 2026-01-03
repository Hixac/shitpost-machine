from typing import Any
from datetime import datetime

from telethon import functions, types
from telethon.sync import TelegramClient
from telethon.tl.types import PeerChannel

from ..core.config import settings
from ..core.exceptions import PostNotFound
from ..core.utility import SIMPLE_FILENAME


TG_API_ID = settings.TG_API_ID
TG_API_HASH = settings.TG_API_HASH
TG_PHONE = settings.TG_PHONE
TG_NAME = settings.TG_NAME


_client = TelegramClient(TG_NAME, TG_API_ID, TG_API_HASH)
_ = _client.start(phone=TG_PHONE)


def _get_client():
    return _client


def get_channels_from_folder() -> list[int]:
    folders = _get_client()(functions.messages.GetDialogFiltersRequest()).filters[1:] 
    peers = next(fld for fld in folders if fld.title.text == "МЕМЫ").include_peers
    channels = [peer.channel_id for peer in peers]
    return channels

class Channel:
    @property
    def do_not_name(self) -> bool:
        return self._do_not_name

    @property
    def name(self) -> str:
        return self._name

    def __init__(self, identifier: str | int, do_not_name: bool = False):
        self._identifier: PeerChannel | str
        if isinstance(identifier, int):
            self._identifier = PeerChannel(identifier)
        else:
            self._identifier = identifier

        self._do_not_name: bool = do_not_name
        self._name: str = str(identifier)
        self._date: datetime | None = None

    def get_date_of_last_post(self) -> datetime | None:
        return self._date

    def get_newest_post(self) -> str:
        for msg in _get_client().iter_messages(self._identifier, limit=100):
            if not msg.fwd_from and msg.photo is not None:
                self._date = msg.date
                return msg.download_media(file=SIMPLE_FILENAME)

        raise PostNotFound("Can't find any post in apparently empty channel.")

    def to_dict(self) -> dict[str, dict[str, Any]]:
        return { self.name: {"do_not_name": self._do_not_name} }
