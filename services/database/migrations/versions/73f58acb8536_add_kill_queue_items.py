"""add kill queue items

Revision ID: 73f58acb8536
Revises: ed180e339924
Create Date: 2026-05-26 18:27:39.468984
"""

from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa


revision: str = '73f58acb8536'
down_revision: str | None = 'ed180e339924'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
