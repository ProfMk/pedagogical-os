"""0011_create_academic_period_event

Revision ID: 4c6f2e9ab411
Revises: 7f3e9c21ab10
Create Date: 2026-03-07
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision: str = "4c6f2e9ab411"
down_revision: Union[str, Sequence[str], None] = "7f3e9c21ab10"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()

    op.execute(
        """
        DO $$
        BEGIN
            IF NOT EXISTS (
                SELECT 1
                FROM pg_type
                WHERE typname = 'academic_period_event_type'
            ) THEN
                CREATE TYPE academic_period_event_type AS ENUM (
                    'PERIOD_CLOSED',
                    'PERIOD_REOPENED'
                );
            END IF;
        END
        $$;
        """
    )

    academic_period_event_type = postgresql.ENUM(
        "PERIOD_CLOSED",
        "PERIOD_REOPENED",
        name="academic_period_event_type",
        create_type=False,
    )

    op.create_table(
        "academic_period_event",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("academic_period_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("event_type", academic_period_event_type, nullable=False),
        sa.Column("reason", sa.Text(), nullable=False),
        sa.Column("performed_by_user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.ForeignKeyConstraint(
            ["academic_period_id"],
            ["academic_period.id"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["performed_by_user_id"],
            ["institutional_user.id"],
            ondelete="RESTRICT",
        ),
    )


def downgrade() -> None:
    op.drop_table("academic_period_event")

    op.execute(
        """
        DO $$
        BEGIN
            IF EXISTS (
                SELECT 1
                FROM pg_type
                WHERE typname = 'academic_period_event_type'
            ) THEN
                DROP TYPE academic_period_event_type;
            END IF;
        END
        $$;
        """
    )
