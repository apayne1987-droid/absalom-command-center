from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    workflow_id: int
    name: str = Field(min_length=1, max_length=255)


class TaskRead(BaseModel):
    id: int
    workflow_id: int
    name: str
    state: str

    model_config = {
        "from_attributes": True
    }
