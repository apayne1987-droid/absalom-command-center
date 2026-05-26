from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from services.database.models.task import Task
from services.database.models.workflow import Workflow


class WorkflowRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, name: str) -> Workflow:
        workflow = Workflow(name=name)

        self.session.add(workflow)

        await self.session.commit()
        await self.session.refresh(workflow)

        return workflow

    async def get_by_id(self, workflow_id: int) -> Workflow | None:
        result = await self.session.execute(
            select(Workflow).where(Workflow.id == workflow_id)
        )

        return result.scalar_one_or_none()

    async def list_all(self) -> list[Workflow]:
        result = await self.session.execute(select(Workflow))

        return list(result.scalars().all())

    async def list_tasks(self, workflow_id: int) -> list[Task]:
        result = await self.session.execute(
            select(Task).where(Task.workflow_id == workflow_id)
        )

        return list(result.scalars().all())

    async def update_state(self, workflow: Workflow, state: str) -> Workflow:
        workflow.state = state

        await self.session.commit()
        await self.session.refresh(workflow)

        return workflow
