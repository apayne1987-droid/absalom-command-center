from pydantic import BaseModel, Field


class WorkflowCreate(BaseModel):
    name: str = Field(min_length=1, max_length=255)


class WorkflowRead(BaseModel):
    id: int
    name: str
    state: str

    model_config = {
        "from_attributes": True
    }
