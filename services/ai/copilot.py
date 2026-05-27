from services.ai.client import get_openai_client
from services.config.settings import settings


async def generate_executive_briefing(
    priorities: list[str],
    metrics: dict[str, int | None],
) -> str:
    client = get_openai_client()

    if client is None:
        return (
            "AI Executive Copilot is installed and routed correctly, but "
            "OPENAI_API_KEY is missing. Add it to .env and rebuild Docker "
            "to enable live AI briefings."
        )

    prompt = f"""
You are the AI Executive Copilot for ABSALOM OS.

Analyze the current operational state.

PRIORITIES:
{priorities}

METRICS:
{metrics}

Return a concise executive briefing with:
1. Operational Summary
2. Main Bottleneck
3. Highest Leverage Focus
4. Kill / Elimination Recommendation
5. Execution Recommendation

Do not be motivational. Be strategic, direct, and useful.
"""

    response = await client.chat.completions.create(
        model=settings.ai_default_model,
        messages=[
            {
                "role": "system",
                "content": "You are an elite executive operations advisor.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=0.4,
    )

    return response.choices[0].message.content or "No response generated."
