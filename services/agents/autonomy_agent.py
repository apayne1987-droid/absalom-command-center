from services.orchestration.graph import runtime_graph


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

    return result
