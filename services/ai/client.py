from openai import AsyncOpenAI

from services.config.settings import settings


client = AsyncOpenAI(api_key=settings.openai_api_key)
