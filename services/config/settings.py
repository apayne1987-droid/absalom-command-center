from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "ABSALOM COMMAND CENTER"
    app_version: str = "14.0.0"
    environment: str = "development"


settings = Settings()
