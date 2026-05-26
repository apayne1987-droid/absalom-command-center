from datetime import UTC, datetime

from sqlalchemy import ForeignKey, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from services.database.base import Base


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)

    workflow_id: Mapped[int] = mapped_column(
        ForeignKey("workflows.id"),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    state: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="CREATED",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
        nullable=False,
    )

    workflow = relationship(
        "Workflow",
        back_populates="tasks",
    )

    execution_logs = relationship(
        "ExecutionLog",
        back_populates="task",
        cascade="all, delete-orphan",
    )
