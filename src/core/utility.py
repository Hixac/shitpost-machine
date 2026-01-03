import time
from pathlib import Path
from enum import Enum

from .config import settings


WHERE_TO_SAVE_FILES = settings.WHERE_TO_SAVE_FILES
SIMPLE_FILENAME = WHERE_TO_SAVE_FILES / "picture.jpg"


def simple_save(content: bytes) -> Path:
    with open(SIMPLE_FILENAME, "wb") as f:
        _ = f.write(content)

    return SIMPLE_FILENAME


def pause(seconds: float):
    time.sleep(seconds)
