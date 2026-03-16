"""
Add academic_period_id to indicator_result

Revision ID: a6f2c9d8b1e4
Revises: 65300a0126db
Create Date: 2026-03-01
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a6f2c9d8b1e4"
down_revision = "65300a0126db"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "indicator_result",
        sa.Column(
            "academic_period_id",
            sa.UUID(),
            nullable=True,
        ),
    )

    op.create_foreign_key(
        "indicator_result_academic_period_id_fkey",
        "indicator_result",
        "academic_period",
        ["academic_period_id"],
        ["id"],
        ondelete="RESTRICT",
    )


def downgrade():
    op.drop_constraint(
        "indicator_result_academic_period_id_fkey",
        "indicator_result",
        type_="foreignkey",
    )

    op.drop_column(
        "indicator_result",
        "academic_period_id",
    )
