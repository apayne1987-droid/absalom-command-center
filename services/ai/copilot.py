from openai import AsyncOpenAI

from services.ai.client import client


async def generate_executive_briefing(
    priorities: list[str],
    metrics: dict,
) -> str:
    prompt = f"""
You are an elite executive operations copilot.

Analyze the following operational state.

PRIORITIES:
{priorities}

METRICS:
{metrics}

Provide:
1. Operational summary
2. Main bottleneck
3. Highest leverage focus
4. Elimination recommendation
5. Execution recommendation

Keep response concise, intelligent, and executive-level.
"""

    response = await client.chat.completions.create(
        model="gpt-4.1-mini",
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
