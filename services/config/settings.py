from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    openai_api_key: str = ""
    ai_default_model: str = "gpt-4.1-mini"
    sentry_dsn: str = ""
    posthog_api_key: str = ""
    ENVIRONMENT: str = "development"

    APP_NAME: str = "ABSALOM OS"
    APP_VERSION: str = "0.1.0"

    DATABASE_URL: str
    REDIS_URL: str

    OPENAI_API_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""

    DEFAULT_MODEL: str = "gpt-4.1-mini"

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

    @property
    def database_url(self) -> str:
        return self.DATABASE_URL

    @property
    def redis_url(self) -> str:
        return self.REDIS_URL

    @property
    def app_name(self) -> str:
        return self.APP_NAME

    @property
    def app_version(self) -> str:
        return self.APP_VERSION


settings = Settings.model_validate({})


