from typing import Literal

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


class Settings(BaseSettings):
    LOG_LEVEL: LogLevel = "INFO"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @field_validator("LOG_LEVEL", mode="before")
    @classmethod
    def normalize_log_level(cls, value: object) -> object:
        if isinstance(value, str):
            return value.strip().upper()
        return value


settings = Settings()
