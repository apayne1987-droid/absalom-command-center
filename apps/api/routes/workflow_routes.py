from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from services.database.session import get_database_session
from services.workflow.schemas.workflow import WorkflowCreate, WorkflowRead
from services.workflow.services.workflow_service import WorkflowService

router = APIRouter(prefix="/workflows", tags=["workflows"])


@router.post("", response_model=WorkflowRead)
async def create_workflow(
    payload: WorkflowCreate,
    session: AsyncSession = Depends(get_database_session),
):
    service = WorkflowService(session)

    return await service.create_workflow(payload)


@router.get("", response_model=list[WorkflowRead])
async def list_workflows(
    session: AsyncSession = Depends(get_database_session),
):
    service = WorkflowService(session)

    return await service.list_workflows()
