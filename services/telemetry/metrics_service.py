from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from services.database.models.execution_log import ExecutionLog
from services.database.models.task import Task
from services.database.models.workflow import Workflow


class MetricsService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_runtime_metrics(self) -> dict[str, int]:
        workflow_count = await self.session.scalar(
            select(func.count()).select_from(Workflow)
        )

        task_count = await self.session.scalar(
            select(func.count()).select_from(Task)
        )

        execution_log_count = await self.session.scalar(
            select(func.count()).select_from(ExecutionLog)
        )

        completed_task_count = await self.session.scalar(
            select(func.count()).select_from(Task).where(
                Task.state == "COMPLETED"
            )
        )

        failed_task_count = await self.session.scalar(
            select(func.count()).select_from(Task).where(
                Task.state == "FAILED"
            )
        )

        active_task_count = await self.session.scalar(
            select(func.count()).select_from(Task).where(
                Task.state == "ACTIVE"
            )
        )

        return {
            "workflows": workflow_count or 0,
            "tasks": task_count or 0,
            "execution_logs": execution_log_count or 0,
            "completed_tasks": completed_task_count or 0,
            "failed_tasks": failed_task_count or 0,
            "active_tasks": active_task_count or 0,
        }
