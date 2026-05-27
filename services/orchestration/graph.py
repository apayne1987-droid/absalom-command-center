from langgraph.graph import StateGraph, END

from services.schemas.execution_state import ExecutionState
from services.execution.executor import execute_step


async def planning_node(state: ExecutionState):

    state["current_step"] = "Strategic Planning"

    result = await execute_step(
        "Strategic Planning"
    )

    state["result"] = result

    return state


async def validation_node(state: ExecutionState):

    state["validation_status"] = "validated"

    return state


graph = StateGraph(ExecutionState)

graph.add_node(
    "planning",
    planning_node,
)

graph.add_node(
    "validation",
    validation_node,
)

graph.set_entry_point("planning")

graph.add_edge(
    "planning",
    "validation",
)

graph.add_edge(
    "validation",
    END,
)

runtime_graph = graph.compile()
