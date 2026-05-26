"""initial runtime schema

Revision ID: 5a38499f6ff5
Revises: 
Create Date: 2026-05-25 23:47:41.248195
"""

from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa


revision: str = '5a38499f6ff5'
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
