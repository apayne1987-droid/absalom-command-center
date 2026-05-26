from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from services.database.models.task import Task


class TaskRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, workflow_id: int, name: str) -> Task:
        task = Task(workflow_id=workflow_id, name=name)

        self.session.add(task)

        await self.session.commit()
        await self.session.refresh(task)

        return task

    async def get_by_id(self, task_id: int) -> Task | None:
        result = await self.session.execute(
            select(Task).where(Task.id == task_id)
        )

        return result.scalar_one_or_none()

    async def update_state(self, task: Task, state: str) -> Task:
        task.state = state

        await self.session.commit()
        await self.session.refresh(task)

        return task

    async def list_all(self) -> list[Task]:
        result = await self.session.execute(select(Task))

        return list(result.scalars().all())
