from openai import AsyncOpenAI

from services.config.settings import settings


def get_openai_client() -> AsyncOpenAI | None:
    if not settings.openai_api_key:
        return None

    return AsyncOpenAI(api_key=settings.openai_api_key)
