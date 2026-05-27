from typing import TypedDict


class ExecutionState(TypedDict):
    objective: str
    current_step: str
    status: str
    result: str
    validation_status: str
    retry_count: int
