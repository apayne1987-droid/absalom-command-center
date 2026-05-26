from openai import AsyncOpenAI

from services.config.settings import settings


client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
