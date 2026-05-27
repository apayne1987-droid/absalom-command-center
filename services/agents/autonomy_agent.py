from services.memory.runtime_trace_store import add_runtime_trace
from services.orchestration.graph import runtime_graph
from services.schemas.runtime_trace import RuntimeTrace


async def run_autonomous_objective(
    objective: str,
):
    result = await runtime_graph.ainvoke(
        {
            "objective": objective,
            "current_step": "",
            "status": "running",
            "result": "",
            "validation_status": "",
            "retry_count": 0,
        }
    )

    add_runtime_trace(
        RuntimeTrace(
            objective=result["objective"],
            current_step=result["current_step"],
            status="completed",
            result=result["result"],
            validation_status=result["validation_status"],
            retry_count=result["retry_count"],
        )
    )

    return result
