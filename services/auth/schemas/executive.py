from pydantic import BaseModel


class ExecutivePriorityCreateRequest(BaseModel):
    title: str
    bottleneck: str | None = None
    roi_score: int = 5
    leverage_score: int = 5
    difficulty_score: int = 5
    automation_score: int = 5
    strategic_alignment_score: int = 5


class ExecutivePriorityResponse(BaseModel):
    id: int
    title: str
    bottleneck: str | None
    roi_score: int
    leverage_score: int
    difficulty_score: int
    automation_score: int
    strategic_alignment_score: int
    status: str
    priority_score: int
