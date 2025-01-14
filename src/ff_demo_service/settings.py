from pydantic import Field
from pydantic_settings import BaseSettings as _BaseSettings


class BaseSettings(
    _BaseSettings,
    env_file=".env",
    env_file_encoding="utf-8",
    extra="ignore",
):
    """Dotenv-aware settings."""


class MiscSettings(BaseSettings):
    title: str = "FF Demo Service"
    base_api_path: str = "/api/ff-demo-service"


class FlagsmithSettings(
    BaseSettings,
    env_prefix="flagsmith_",
):
    environment_key: str = ""
    base_url: str = ""
    flags_path: str = ""


class Settings(BaseSettings):
    misc: MiscSettings = Field(default_factory=MiscSettings)
    flagsmith: FlagsmithSettings = Field(default_factory=FlagsmithSettings)


settings = Settings()
