from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    environment: str = "development"

    openai_api_key: str = ""
    ai_default_model: str = "gpt-4.1-mini"

    sentry_dsn: str = ""
    posthog_api_key: str = ""

    database_url: str = ""
    redis_url: str = ""


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
