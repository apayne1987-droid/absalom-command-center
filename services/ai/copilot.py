from services.ai.provider import generate_ai_response


async def generate_executive_briefing(
    priorities: list[str],
    metrics: dict,
) -> str:
    prompt = f"""
Analyze this operational state.

PRIORITIES:
{priorities}

METRICS:
{metrics}

Return:
1. Operational summary
2. Main bottleneck
3. Highest leverage focus
4. Elimination recommendation
5. Execution recommendation

Keep concise and executive-level.
"""

    return await generate_ai_response(
        system_prompt="""
You are an elite executive operational intelligence copilot.
You optimize for leverage, execution, prioritization,
operational compression, and strategic clarity.
""",
        user_prompt=prompt,
    )
