from datetime import UTC, datetime

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from services.database.base import Base


class KillQueueItem(Base):
    __tablename__ = "kill_queue_items"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    reason: Mapped[str | None] = mapped_column(Text, nullable=True)
    drag_score: Mapped[int] = mapped_column(Integer, default=5, nullable=False)
    complexity_score: Mapped[int] = mapped_column(Integer, default=5, nullable=False)
    leverage_loss_score: Mapped[int] = mapped_column(Integer, default=5, nullable=False)
    status: Mapped[str] = mapped_column(String(50), default="REVIEW", nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False,
    )
