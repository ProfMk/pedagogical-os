"""0009_indicator_result_override_audit

Create audit table for indicator_result overrides.

Revision ID: d1b7c3a9f001
Revises: c9e4d2a7f6b1
Create Date: 2026-03-04
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers
revision: str = "d1b7c3a9f001"
down_revision: Union[str, Sequence[str], None] = "c9e4d2a7f6b1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    # =====================================================
    # INDICATOR RESULT OVERRIDE AUDIT TABLE
    # =====================================================

    op.create_table(
        "indicator_result_override",

        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True
        ),

        sa.Column(
            "indicator_result_id",
            postgresql.UUID(as_uuid=True),
            nullable=False
        ),

        sa.Column(
            "override_by_user_id",
            postgresql.UUID(as_uuid=True),
            nullable=False
        ),

        sa.Column(
            "new_final_level",
            sa.Numeric(5, 2),
            nullable=False
        ),

        sa.Column(
            "override_comment",
            sa.Text(),
            nullable=False
        ),

        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            server_default=sa.text("now()")
        ),

        sa.ForeignKeyConstraint(
            ["indicator_result_id"],
            ["indicator_result.id"],
            ondelete="CASCADE"
        ),

        sa.ForeignKeyConstraint(
            ["override_by_user_id"],
            ["institutional_user.id"],
            ondelete="RESTRICT"
        ),
    )

    # =====================================================
    # INDEXES FOR AUDIT PERFORMANCE
    # =====================================================

    op.create_index(
        "ix_override_indicator_result",
        "indicator_result_override",
        ["indicator_result_id"]
    )

    op.create_index(
        "ix_override_user",
        "indicator_result_override",
        ["override_by_user_id"]
    )

    op.create_index(
        "ix_override_created_at",
        "indicator_result_override",
        ["created_at"]
    )


def downgrade() -> None:
    raise NotImplementedError("Downgrade not supported.")