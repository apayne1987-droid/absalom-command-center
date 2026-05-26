from sqlalchemy.ext.asyncio import AsyncSession

from services.workflow.repositories.workflow_repository import WorkflowRepository
from services.workflow.schemas.workflow import WorkflowCreate
from services.database.models.workflow import Workflow


class WorkflowService:
    def __init__(self, session: AsyncSession):
        self.repository = WorkflowRepository(session)

    async def create_workflow(self, payload: WorkflowCreate) -> Workflow:
        return await self.repository.create(name=payload.name)

    async def list_workflows(self) -> list[Workflow]:
        return await self.repository.list_all()
