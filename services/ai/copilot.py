import json

from pydantic import ValidationError

from services.ai.client import get_openai_client
from services.ai.schemas import ExecutiveBriefingStructuredResponse
from services.config.settings import settings


async def generate_executive_briefing(
    priorities: list[str],
    metrics: dict,
    kill_queue: list[str] | None = None,
    weekly_reviews: list[str] | None = None,
) -> ExecutiveBriefingStructuredResponse:
    client = get_openai_client()

    if client is None:
        return ExecutiveBriefingStructuredResponse(
            summary="OPENAI_API_KEY missing.",
            bottleneck="AI runtime unavailable.",
            highest_leverage_focus="Configure OpenAI credentials.",
            kill_recommendation="Do not expand scope yet.",
            execution_recommendation="Add API key and rebuild containers.",
        )

    prompt = f"""
Return ONLY valid JSON.

Schema:
{{
  "summary": "string",
  "bottleneck": "string",
  "highest_leverage_focus": "string",
  "kill_recommendation": "string",
  "execution_recommendation": "string"
}}

PRIORITIES:
{priorities}

METRICS:
{metrics}

KILL_QUEUE:
{kill_queue or []}

WEEKLY_REVIEWS:
{weekly_reviews or []}
"""

    response = await client.chat.completions.create(
        model=settings.ai_default_model,
        response_format={"type": "json_object"},
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
        temperature=0.2,
    )

    content = response.choices[0].message.content or "{}"

    try:
        parsed = json.loads(content)
        return ExecutiveBriefingStructuredResponse(**parsed)

    except (json.JSONDecodeError, ValidationError):
        return ExecutiveBriefingStructuredResponse(
            summary="AI response formatting failure.",
            bottleneck="Invalid structured response.",
            highest_leverage_focus="Stabilize AI output parsing.",
            kill_recommendation="Avoid orchestration complexity.",
            execution_recommendation="Inspect AI output manually.",
        )
