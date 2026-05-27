from datetime import datetime

from pydantic import BaseModel, ConfigDict


class RuntimeTrace(BaseModel):
    id: int | None = None
    objective: str
    current_step: str
    status: str
    result: str
    validation_status: str
    retry_count: int
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)
