from fastapi import APIRouter

from services.agents.autonomy_agent import run_autonomous_objective
from services.memory.runtime_trace_store import get_runtime_traces
from services.schemas.runtime_trace import RuntimeTrace


router = APIRouter(
    prefix="/autonomy",
    tags=["autonomy"],
)


@router.post("/execute")
async def execute_objective(
    payload: dict,
):
    objective = payload.get("objective", "")

    result = await run_autonomous_objective(objective)

    return result


@router.get(
    "/traces",
    response_model=list[RuntimeTrace],
)
async def list_traces():
    return get_runtime_traces()
