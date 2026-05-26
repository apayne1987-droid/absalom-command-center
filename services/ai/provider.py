from litellm import acompletion

from services.config.settings import settings


async def generate_ai_response(
    *,
    system_prompt: str,
    user_prompt: str,
    model: str | None = None,
) -> str:
    response = await acompletion(
        model=model or settings.DEFAULT_MODEL,
        api_key=settings.OPENAI_API_KEY,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
        temperature=0.4,
    )

    return response["choices"][0]["message"]["content"]
