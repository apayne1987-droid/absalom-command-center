from fastapi import APIRouter

from services.ai.copilot import generate_executive_briefing
from services.schemas.copilot import ExecutiveBriefing


router = APIRouter(
    prefix="/copilot",
    tags=["copilot"],
)


@router.get("/briefing", response_model=ExecutiveBriefing)
async def get_briefing():
    return await generate_executive_briefing()
