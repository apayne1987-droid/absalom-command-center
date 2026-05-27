from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from services.ai.copilot import generate_executive_briefing
from services.ai.schemas import ExecutiveBriefingStructuredResponse
from services.auth.dependencies import get_current_user
from services.database.models.execution_log import ExecutionLog
from services.database.models.executive_priority import ExecutivePriority
from services.database.models.kill_queue_item import KillQueueItem
from services.database.models.task import Task
from services.database.models.user import User
from services.database.models.weekly_review import WeeklyReview
from services.database.models.workflow import Workflow
from services.database.session import get_db


router = APIRouter(
    prefix="/copilot",
    tags=["copilot"],
)


@router.get(
    "/briefing",
    response_model=ExecutiveBriefingStructuredResponse,
)
async def executive_briefing(
    session: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    priorities_result = await session.scalars(
        select(ExecutivePriority.title)
    )

    priorities = list(priorities_result)

    kill_result = await session.scalars(
        select(KillQueueItem.title)
    )

    kill_queue = list(kill_result)

    reviews_result = await session.scalars(
        select(WeeklyReview.next_priorities)
        .order_by(WeeklyReview.id.desc())
        .limit(3)
    )

    weekly_reviews = list(reviews_result)

    workflows = await session.scalar(
        select(func.count()).select_from(Workflow)
    ) or 0

    tasks = await session.scalar(
        select(func.count()).select_from(Task)
    ) or 0

    logs = await session.scalar(
        select(func.count()).select_from(ExecutionLog)
    ) or 0

    metrics = {
        "workflows": workflows,
        "tasks": tasks,
        "execution_logs": logs,
    }

    return await generate_executive_briefing(
        priorities=priorities,
        metrics=metrics,
        kill_queue=kill_queue,
        weekly_reviews=weekly_reviews,
    )
