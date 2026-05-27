from pydantic import BaseModel, Field


class ExecutiveBriefingStructuredResponse(BaseModel):
    summary: str = Field(..., max_length=5000)
    bottleneck: str = Field(..., max_length=5000)
    highest_leverage_focus: str = Field(..., max_length=5000)
    kill_recommendation: str = Field(..., max_length=5000)
    execution_recommendation: str = Field(..., max_length=5000)
