from fastapi import APIRouter

from services.ai.priority_engine import get_priority_items
from services.schemas.priority import PriorityItem


router = APIRouter(
    prefix="/priority",
    tags=["priority"],
)


@router.get(
    "/rankings",
    response_model=list[PriorityItem],
)
async def get_rankings():
    return get_priority_items()
