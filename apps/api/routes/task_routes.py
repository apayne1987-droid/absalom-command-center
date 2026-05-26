from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from services.database.session import get_database_session
from services.task.schemas.task import (
    TaskCreate,
    TaskDispatchRead,
    TaskRead,
    TaskUpdateState,
)
from services.task.services.task_dispatch_service import TaskDispatchService
from services.task.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("", response_model=TaskRead)
async def create_task(
    payload: TaskCreate,
    session: AsyncSession = Depends(get_database_session),
):
    service = TaskService(session)

    return await service.create_task(payload)


@router.get("", response_model=list[TaskRead])
async def list_tasks(
    session: AsyncSession = Depends(get_database_session),
):
    service = TaskService(session)

    return await service.list_tasks()


@router.patch("/{task_id}/state", response_model=TaskRead)
async def update_task_state(
    task_id: int,
    payload: TaskUpdateState,
    session: AsyncSession = Depends(get_database_session),
):
    service = TaskService(session)

    return await service.update_task_state(
        task_id=task_id,
        state=payload.state,
    )


@router.post("/{task_id}/dispatch", response_model=TaskDispatchRead)
async def dispatch_task(task_id: int):
    dispatch_service = TaskDispatchService()
    result = dispatch_service.dispatch_task(task_id)

    return {
        "task_id": task_id,
        "dispatch_id": result.id,
        "status": "dispatched",
    }
