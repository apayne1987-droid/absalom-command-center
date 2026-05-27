from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from services.agents.autonomy_agent import run_autonomous_objective
from services.database.models.runtime_trace import RuntimeTraceRecord
from services.database.session import get_db
from services.schemas.runtime_trace import RuntimeTrace


router = APIRouter(
    prefix="/autonomy",
    tags=["autonomy"],
)


@router.post("/execute")
async def execute_objective(
    payload: dict,
    session: AsyncSession = Depends(get_db),
):
    objective = payload.get("objective", "")

    result = await run_autonomous_objective(objective)

    trace = RuntimeTraceRecord(
        objective=result["objective"],
        current_step=result["current_step"],
        status="completed",
        result=result["result"],
        validation_status=result["validation_status"],
        retry_count=result["retry_count"],
    )

    session.add(trace)

    await session.commit()
    await session.refresh(trace)

    return RuntimeTrace.model_validate(trace)


@router.get(
    "/traces",
    response_model=list[RuntimeTrace],
)
async def list_traces(
    session: AsyncSession = Depends(get_db),
):
    result = await session.scalars(
        select(RuntimeTraceRecord).order_by(
            RuntimeTraceRecord.id.desc()
        ).limit(25)
    )

    return list(result)
