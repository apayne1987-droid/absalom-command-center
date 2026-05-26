from sqlalchemy.ext.asyncio import AsyncSession

from services.database.models.execution_log import ExecutionLog
from services.execution.repositories.execution_log_repository import ExecutionLogRepository
from services.execution.schemas.execution_log import ExecutionLogCreate


class ExecutionLogService:
    def __init__(self, session: AsyncSession):
        self.repository = ExecutionLogRepository(session)

    async def create_log(self, payload: ExecutionLogCreate) -> ExecutionLog:
        return await self.repository.create(
            task_id=payload.task_id,
            event_type=payload.event_type,
            message=payload.message,
        )

    async def create_system_log(
        self,
        task_id: int,
        event_type: str,
        message: str,
    ) -> ExecutionLog:
        return await self.repository.create(
            task_id=task_id,
            event_type=event_type,
            message=message,
        )

    async def list_logs(self) -> list[ExecutionLog]:
        return await self.repository.list_all()

    async def list_logs_by_task(self, task_id: int) -> list[ExecutionLog]:
        return await self.repository.list_by_task(task_id)
