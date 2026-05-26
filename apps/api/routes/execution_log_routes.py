from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from services.database.session import get_database_session
from services.execution.schemas.execution_log import ExecutionLogCreate, ExecutionLogRead
from services.execution.services.execution_log_service import ExecutionLogService

router = APIRouter(prefix="/execution-logs", tags=["execution-logs"])


@router.post("", response_model=ExecutionLogRead)
async def create_execution_log(
    payload: ExecutionLogCreate,
    session: AsyncSession = Depends(get_database_session),
):
    service = ExecutionLogService(session)

    return await service.create_log(payload)


@router.get("", response_model=list[ExecutionLogRead])
async def list_execution_logs(
    session: AsyncSession = Depends(get_database_session),
):
    service = ExecutionLogService(session)

    return await service.list_logs()


@router.get("/task/{task_id}", response_model=list[ExecutionLogRead])
async def list_execution_logs_by_task(
    task_id: int,
    session: AsyncSession = Depends(get_database_session),
):
    service = ExecutionLogService(session)

    return await service.list_logs_by_task(task_id)
