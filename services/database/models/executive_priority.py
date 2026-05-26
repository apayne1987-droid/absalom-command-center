from datetime import UTC, datetime

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from services.database.base import Base


class ExecutivePriority(Base):
    __tablename__ = "executive_priorities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    bottleneck: Mapped[str | None] = mapped_column(Text, nullable=True)
    roi_score: Mapped[int] = mapped_column(Integer, default=5, nullable=False)
    leverage_score: Mapped[int] = mapped_column(Integer, default=5, nullable=False)
    difficulty_score: Mapped[int] = mapped_column(Integer, default=5, nullable=False)
    automation_score: Mapped[int] = mapped_column(Integer, default=5, nullable=False)
    strategic_alignment_score: Mapped[int] = mapped_column(Integer, default=5, nullable=False)
    status: Mapped[str] = mapped_column(String(50), default="ACTIVE", nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False,
    )
