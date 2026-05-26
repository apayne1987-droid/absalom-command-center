from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from services.database.models.execution_log import ExecutionLog


class ExecutionLogRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(
        self,
        task_id: int,
        event_type: str,
        message: str,
    ) -> ExecutionLog:
        log = ExecutionLog(
            task_id=task_id,
            event_type=event_type,
            message=message,
        )

        self.session.add(log)

        await self.session.commit()
        await self.session.refresh(log)

        return log

    async def list_all(self) -> list[ExecutionLog]:
        result = await self.session.execute(select(ExecutionLog))

        return list(result.scalars().all())

    async def list_by_task(self, task_id: int) -> list[ExecutionLog]:
        result = await self.session.execute(
            select(ExecutionLog).where(ExecutionLog.task_id == task_id)
        )

        return list(result.scalars().all())
