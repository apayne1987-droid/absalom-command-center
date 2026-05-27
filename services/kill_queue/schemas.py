from pydantic import BaseModel


class KillQueueCreateRequest(BaseModel):
    title: str
    reason: str | None = None
    drag_score: int = 5
    complexity_score: int = 5
    leverage_loss_score: int = 5


class KillQueueResponse(BaseModel):
    id: int
    title: str
    reason: str | None
    drag_score: int
    complexity_score: int
    leverage_loss_score: int
    status: str
    kill_score: int
