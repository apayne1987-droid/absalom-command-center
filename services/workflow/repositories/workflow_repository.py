from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

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

    async def list_all(self) -> list[Workflow]:
        result = await self.session.execute(select(Workflow))

        return list(result.scalars().all())
