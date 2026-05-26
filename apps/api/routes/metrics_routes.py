from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from services.database.session import get_database_session
from services.telemetry.metrics_service import MetricsService

router = APIRouter(
    prefix="/metrics",
    tags=["metrics"],
)


@router.get("/runtime")
async def get_runtime_metrics(
    session: AsyncSession = Depends(get_database_session),
):
    service = MetricsService(session)

    return await service.get_runtime_metrics()
