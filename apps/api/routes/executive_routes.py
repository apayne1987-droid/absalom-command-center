from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from services.auth.dependencies import get_current_user
from services.auth.schemas.executive import (
    ExecutivePriorityCreateRequest,
    ExecutivePriorityResponse,
)
from services.database.models.executive_priority import ExecutivePriority
from services.database.models.user import User
from services.database.session import get_db


router = APIRouter(prefix="/executive", tags=["executive"])


def calculate_priority_score(priority: ExecutivePriority) -> int:
    return (
        priority.roi_score
        + priority.leverage_score
        + priority.automation_score
        + priority.strategic_alignment_score
        - priority.difficulty_score
    )


@router.get("/priorities", response_model=list[ExecutivePriorityResponse])
async def list_priorities(
    session: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await session.scalars(
        select(ExecutivePriority).order_by(ExecutivePriority.id.desc())
    )

    priorities = list(result)

    return [
        ExecutivePriorityResponse(
            id=priority.id,
            title=priority.title,
            bottleneck=priority.bottleneck,
            roi_score=priority.roi_score,
            leverage_score=priority.leverage_score,
            difficulty_score=priority.difficulty_score,
            automation_score=priority.automation_score,
            strategic_alignment_score=priority.strategic_alignment_score,
            status=priority.status,
            priority_score=calculate_priority_score(priority),
        )
        for priority in priorities
    ]


@router.post("/priorities", response_model=ExecutivePriorityResponse)
async def create_priority(
    payload: ExecutivePriorityCreateRequest,
    session: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    priority = ExecutivePriority(
        title=payload.title,
        bottleneck=payload.bottleneck,
        roi_score=payload.roi_score,
        leverage_score=payload.leverage_score,
        difficulty_score=payload.difficulty_score,
        automation_score=payload.automation_score,
        strategic_alignment_score=payload.strategic_alignment_score,
    )

    session.add(priority)

    await session.commit()
    await session.refresh(priority)

    return ExecutivePriorityResponse(
        id=priority.id,
        title=priority.title,
        bottleneck=priority.bottleneck,
        roi_score=priority.roi_score,
        leverage_score=priority.leverage_score,
        difficulty_score=priority.difficulty_score,
        automation_score=priority.automation_score,
        strategic_alignment_score=priority.strategic_alignment_score,
        status=priority.status,
        priority_score=calculate_priority_score(priority),
    )
