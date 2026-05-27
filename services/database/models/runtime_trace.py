from datetime import UTC, datetime

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from services.database.base import Base


class RuntimeTraceRecord(Base):
    __tablename__ = "runtime_traces"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    objective: Mapped[str] = mapped_column(Text, nullable=False)
    current_step: Mapped[str] = mapped_column(String(255), nullable=False)
    status: Mapped[str] = mapped_column(String(100), nullable=False)
    result: Mapped[str] = mapped_column(Text, nullable=False)
    validation_status: Mapped[str] = mapped_column(String(100), nullable=False)
    retry_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False,
    )
