"""
Make academic_period_id NOT NULL in indicator_result

Revision ID: b7d3f1e2c9a4
Revises: a6f2c9d8b1e4
Create Date: 2026-03-01
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b7d3f1e2c9a4"
down_revision = "a6f2c9d8b1e4"
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        "indicator_result",
        "academic_period_id",
        existing_type=sa.UUID(),
        nullable=False,
    )


def downgrade():
    op.alter_column(
        "indicator_result",
        "academic_period_id",
        existing_type=sa.UUID(),
        nullable=True,
    )
