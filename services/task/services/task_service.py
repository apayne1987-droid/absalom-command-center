from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from services.database.models.task import Task
from services.execution.services.execution_log_service import ExecutionLogService
from services.task.repositories.task_repository import TaskRepository
from services.task.schemas.task import TaskCreate
from services.workflow.services.workflow_service import WorkflowService


VALID_TASK_STATES = {
    "CREATED",
    "QUEUED",
    "ACTIVE",
    "PAUSED",
    "COMPLETED",
    "FAILED",
    "ARCHIVED",
}


class TaskService:
    def __init__(self, session: AsyncSession):
        self.repository = TaskRepository(session)
        self.execution_log_service = ExecutionLogService(session)
        self.workflow_service = WorkflowService(session)

    async def create_task(self, payload: TaskCreate) -> Task:
        task = await self.repository.create(
            workflow_id=payload.workflow_id,
            name=payload.name,
        )

        await self.execution_log_service.create_system_log(
            task_id=task.id,
            event_type="task.created",
            message=f"Task created: {task.name}",
        )

        await self.workflow_service.recalculate_workflow_state(task.workflow_id)

        return task

    async def list_tasks(self) -> list[Task]:
        return await self.repository.list_all()

    async def update_task_state(self, task_id: int, state: str) -> Task:
        normalized_state = state.upper()

        if normalized_state not in VALID_TASK_STATES:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid task state: {state}",
            )

        task = await self.repository.get_by_id(task_id)

        if task is None:
            raise HTTPException(
                status_code=404,
                detail=f"Task not found: {task_id}",
            )

        updated_task = await self.repository.update_state(task, normalized_state)

        await self.execution_log_service.create_system_log(
            task_id=updated_task.id,
            event_type="task.state_updated",
            message=f"Task state changed to {normalized_state}",
        )

        await self.workflow_service.recalculate_workflow_state(
            updated_task.workflow_id
        )

        return updated_task
