from sqlalchemy.ext.asyncio import AsyncSession

from services.database.models.task import Task
from services.task.repositories.task_repository import TaskRepository
from services.task.schemas.task import TaskCreate


class TaskService:
    def __init__(self, session: AsyncSession):
        self.repository = TaskRepository(session)

    async def create_task(self, payload: TaskCreate) -> Task:
        return await self.repository.create(
            workflow_id=payload.workflow_id,
            name=payload.name,
        )

    async def list_tasks(self) -> list[Task]:
        return await self.repository.list_all()
