from fastapi import APIRouter

from services.agents.autonomy_agent import (
    run_autonomous_objective,
)


router = APIRouter(
    prefix="/autonomy",
    tags=["autonomy"],
)


@router.post("/execute")
async def execute_objective(
    payload: dict,
):

    objective = payload.get("objective")

    result = await run_autonomous_objective(
        objective
    )

    return result
