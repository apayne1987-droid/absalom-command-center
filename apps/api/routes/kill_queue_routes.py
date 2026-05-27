from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from services.auth.dependencies import get_current_user
from services.database.models.kill_queue_item import KillQueueItem
from services.database.models.user import User
from services.database.session import get_db
from services.kill_queue.schemas import (
    KillQueueCreateRequest,
    KillQueueResponse,
)


router = APIRouter(prefix="/kill-queue", tags=["kill-queue"])


def calculate_kill_score(item: KillQueueItem) -> int:
    return (
        item.drag_score
        + item.complexity_score
        + item.leverage_loss_score
    )


@router.get("", response_model=list[KillQueueResponse])
async def list_kill_queue_items(
    session: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    result = await session.scalars(
        select(KillQueueItem).order_by(KillQueueItem.id.desc())
    )

    items = list(result)

    return [
        KillQueueResponse(
            id=item.id,
            title=item.title,
            reason=item.reason,
            drag_score=item.drag_score,
            complexity_score=item.complexity_score,
            leverage_loss_score=item.leverage_loss_score,
            status=item.status,
            kill_score=calculate_kill_score(item),
        )
        for item in items
    ]


@router.post("", response_model=KillQueueResponse)
async def create_kill_queue_item(
    payload: KillQueueCreateRequest,
    session: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    item = KillQueueItem(
        title=payload.title,
        reason=payload.reason,
        drag_score=payload.drag_score,
        complexity_score=payload.complexity_score,
        leverage_loss_score=payload.leverage_loss_score,
    )

    session.add(item)

    await session.commit()
    await session.refresh(item)

    return KillQueueResponse(
        id=item.id,
        title=item.title,
        reason=item.reason,
        drag_score=item.drag_score,
        complexity_score=item.complexity_score,
        leverage_loss_score=item.leverage_loss_score,
        status=item.status,
        kill_score=calculate_kill_score(item),
    )
