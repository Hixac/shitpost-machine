import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class RedditSettings(BaseSettings):
    RED_CLIENT_ID: str
    RED_CLIENT_SECRET: str
    RED_USER_AGENT: str


class TelegramSettings(BaseSettings):
    TG_API_ID: int
    TG_API_HASH: str
    TG_PHONE: str
    TG_NAME: str


class VkSettings(BaseSettings):
    USER_TOKEN: str
    GROUP_ID: int


class Settings(TelegramSettings, VkSettings, RedditSettings):
    WHERE_TO_SAVE_FILES: Path

    model_config = SettingsConfigDict(
            env_file=os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", ".env"),
            env_file_encoding="utf-8",
            case_sensitive=True,
            extra="ignore",
    )


settings = Settings()
