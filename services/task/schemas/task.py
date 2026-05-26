from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    workflow_id: int
    name: str = Field(min_length=1, max_length=255)


class TaskUpdateState(BaseModel):
    state: str = Field(min_length=1, max_length=50)


class TaskRead(BaseModel):
    id: int
    workflow_id: int
    name: str
    state: str

    model_config = {
        "from_attributes": True
    }


class TaskDispatchRead(BaseModel):
    task_id: int
    dispatch_id: str
    status: str
