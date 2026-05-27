from pydantic import BaseModel


class PriorityItem(BaseModel):
    title: str
    roi_score: int
    leverage_score: int
    automation_score: int
    strategic_alignment_score: int
    difficulty_score: int
    priority_score: int
