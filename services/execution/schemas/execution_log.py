from pydantic import BaseModel, Field


class ExecutionLogCreate(BaseModel):
    task_id: int
    event_type: str = Field(min_length=1, max_length=100)
    message: str = Field(min_length=1)


class ExecutionLogRead(BaseModel):
    id: int
    task_id: int
    event_type: str
    message: str

    model_config = {
        "from_attributes": True
    }
