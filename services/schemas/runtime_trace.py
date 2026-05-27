from pydantic import BaseModel


class RuntimeTrace(BaseModel):
    objective: str
    current_step: str
    status: str
    result: str
    validation_status: str
    retry_count: int
