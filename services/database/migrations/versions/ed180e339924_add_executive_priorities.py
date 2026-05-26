"""add executive priorities

Revision ID: ed180e339924
Revises: dc329d48e915
Create Date: 2026-05-26 14:24:38.964478
"""

from collections.abc import Sequence



revision: str = 'ed180e339924'
down_revision: str | None = 'dc329d48e915'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
