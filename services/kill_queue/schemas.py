from enum import Enum

from pydantic import BaseModel, Field


class KillQueueStatus(str, Enum):
    REVIEW = "REVIEW"
    KEEP = "KEEP"
    KILL = "KILL"
    AUTOMATE = "AUTOMATE"


class KillQueueCreateRequest(BaseModel):
    title: str = Field(..., min_length=3, max_length=200)

    reason: str | None = Field(
        default=None,
        max_length=2000,
    )

    drag_score: int = Field(default=5, ge=1, le=10)

    complexity_score: int = Field(
        default=5,
        ge=1,
        le=10,
    )

    leverage_loss_score: int = Field(
        default=5,
        ge=1,
        le=10,
    )

    status: KillQueueStatus = KillQueueStatus.REVIEW
