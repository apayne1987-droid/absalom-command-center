from pydantic import BaseModel


class ExecutiveBriefingResponse(BaseModel):
    summary: str
