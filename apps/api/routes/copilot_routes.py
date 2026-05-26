from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from services.ai.copilot import generate_executive_briefing
from services.ai.schemas import ExecutiveBriefingResponse
from services.auth.dependencies import get_current_user
from services.database.models.execution_log import ExecutionLog
from services.database.models.executive_priority import ExecutivePriority
from services.database.models.task import Task
from services.database.models.user import User
from services.database.models.workflow import Workflow
from services.database.session import get_db


router = APIRouter(prefix="/copilot", tags=["copilot"])


@router.get("/briefing", response_model=ExecutiveBriefingResponse)
async def executive_briefing(
    session: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    priorities_result = await session.scalars(
        select(ExecutivePriority.title)
    )

    priorities = list(priorities_result)

    workflows = await session.scalar(
        select(func.count()).select_from(Workflow)
    )

    tasks = await session.scalar(
        select(func.count()).select_from(Task)
    )

    logs = await session.scalar(
        select(func.count()).select_from(ExecutionLog)
    )

    metrics = {
        "workflows": workflows,
        "tasks": tasks,
        "execution_logs": logs,
    }

    briefing = await generate_executive_briefing(
        priorities=priorities,
        metrics=metrics,
    )

    return ExecutiveBriefingResponse(summary=briefing)
