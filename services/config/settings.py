import os

from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "ABSALOM COMMAND CENTER"
    app_version: str = "14.0.0"
    environment: str = os.getenv("ENVIRONMENT", "development")
    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql+asyncpg://absalom:absalom@localhost:5432/absalom_command_center",
    )


settings = Settings()
