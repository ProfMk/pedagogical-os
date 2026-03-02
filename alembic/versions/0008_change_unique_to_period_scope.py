"""
Change UNIQUE constraint from year scope to period scope in indicator_result

Revision ID: c9e4d2a7f6b1
Revises: b7d3f1e2c9a4
Create Date: 2026-03-01
"""

from alembic import op


# revision identifiers, used by Alembic.
revision = "c9e4d2a7f6b1"
down_revision = "b7d3f1e2c9a4"
branch_labels = None
depends_on = None


def upgrade():
    # 1️⃣ Drop old UNIQUE constraint
    op.drop_constraint(
        "uq_indicator_result_per_year",
        "indicator_result",
        type_="unique",
    )

    # 2️⃣ Create new UNIQUE constraint scoped to period
    op.create_unique_constraint(
        "uq_indicator_result_per_period",
        "indicator_result",
        ["student_id", "indicator_id", "academic_period_id"],
    )


def downgrade():
    # 1️⃣ Drop new UNIQUE
    op.drop_constraint(
        "uq_indicator_result_per_period",
        "indicator_result",
        type_="unique",
    )

    # 2️⃣ Restore original UNIQUE
    op.create_unique_constraint(
        "uq_indicator_result_per_year",
        "indicator_result",
        ["student_id", "indicator_id", "academic_year_id"],
    )