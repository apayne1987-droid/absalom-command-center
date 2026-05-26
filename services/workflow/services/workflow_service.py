from sqlalchemy.ext.asyncio import AsyncSession

from services.database.models.workflow import Workflow
from services.workflow.repositories.workflow_repository import WorkflowRepository
from services.workflow.schemas.workflow import WorkflowCreate


class WorkflowService:
    def __init__(self, session: AsyncSession):
        self.repository = WorkflowRepository(session)

    async def create_workflow(self, payload: WorkflowCreate) -> Workflow:
        return await self.repository.create(name=payload.name)

    async def list_workflows(self) -> list[Workflow]:
        return await self.repository.list_all()

    async def recalculate_workflow_state(self, workflow_id: int) -> Workflow | None:
        workflow = await self.repository.get_by_id(workflow_id)

        if workflow is None:
            return None

        tasks = await self.repository.list_tasks(workflow_id)

        if not tasks:
            return workflow

        task_states = {task.state for task in tasks}

        if task_states == {"COMPLETED"}:
            return await self.repository.update_state(workflow, "COMPLETED")

        if "FAILED" in task_states:
            return await self.repository.update_state(workflow, "FAILED")

        if "ACTIVE" in task_states or "QUEUED" in task_states:
            return await self.repository.update_state(workflow, "ACTIVE")

        return await self.repository.update_state(workflow, "CREATED")
