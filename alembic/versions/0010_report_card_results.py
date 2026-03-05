"""0010_report_card_results

Create report card tables for nucleus and subject results.

Revision ID: 7f3e9c21ab10
Revises: d1b7c3a9f001
Create Date: 2026-03-04
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers
revision: str = "7f3e9c21ab10"
down_revision: Union[str, Sequence[str], None] = "d1b7c3a9f001"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    # =====================================================
    # REPORT CARD NUCLEUS RESULT
    # =====================================================

    op.create_table(
        "report_card_nucleus_result",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),

        sa.Column("student_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("subject_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("nucleus_id", postgresql.UUID(as_uuid=True), nullable=False),

        sa.Column("academic_period_id", postgresql.UUID(as_uuid=True), nullable=False),

        sa.Column("calculated_grade", sa.Numeric(5,2), nullable=False),
        sa.Column("final_grade", sa.Numeric(5,2), nullable=False),

        sa.Column("teacher_observation", sa.Text()),

        sa.Column("override_flag", sa.Boolean(), nullable=False),

        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),

        sa.ForeignKeyConstraint(
            ["student_id"],
            ["student.id"],
            ondelete="CASCADE"
        ),

        sa.ForeignKeyConstraint(
            ["subject_id"],
            ["subject.id"],
            ondelete="RESTRICT"
        ),

        sa.ForeignKeyConstraint(
            ["nucleus_id"],
            ["nucleus.id"],
            ondelete="RESTRICT"
        ),

        sa.ForeignKeyConstraint(
            ["academic_period_id"],
            ["academic_period.id"],
            ondelete="CASCADE"
        ),

        sa.UniqueConstraint(
            "student_id",
            "nucleus_id",
            "academic_period_id",
            name="uq_report_card_nucleus"
        ),
    )


    # =====================================================
    # REPORT CARD SUBJECT RESULT
    # =====================================================

    op.create_table(
        "report_card_subject_result",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),

        sa.Column("student_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("subject_id", postgresql.UUID(as_uuid=True), nullable=False),

        sa.Column("academic_period_id", postgresql.UUID(as_uuid=True), nullable=False),

        sa.Column("calculated_grade", sa.Numeric(5,2), nullable=False),
        sa.Column("final_grade", sa.Numeric(5,2), nullable=False),

        sa.Column("teacher_observation", sa.Text()),

        sa.Column("override_flag", sa.Boolean(), nullable=False),

        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),

        sa.ForeignKeyConstraint(
            ["student_id"],
            ["student.id"],
            ondelete="CASCADE"
        ),

        sa.ForeignKeyConstraint(
            ["subject_id"],
            ["subject.id"],
            ondelete="RESTRICT"
        ),

        sa.ForeignKeyConstraint(
            ["academic_period_id"],
            ["academic_period.id"],
            ondelete="CASCADE"
        ),

        sa.UniqueConstraint(
            "student_id",
            "subject_id",
            "academic_period_id",
            name="uq_report_card_subject"
        ),
    )


    # =====================================================
    # OVERRIDE AUDIT
    # =====================================================

    op.create_table(
        "report_card_override",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),

        sa.Column("entity_type", sa.String(20), nullable=False),
        sa.Column("entity_id", postgresql.UUID(as_uuid=True), nullable=False),

        sa.Column("override_by_user_id", postgresql.UUID(as_uuid=True), nullable=False),

        sa.Column("previous_grade", sa.Numeric(5,2), nullable=False),
        sa.Column("new_grade", sa.Numeric(5,2), nullable=False),

        sa.Column("override_comment", sa.Text(), nullable=False),

        sa.Column("created_at", sa.DateTime(), nullable=False, server_default=sa.text("now()")),

        sa.ForeignKeyConstraint(
            ["override_by_user_id"],
            ["institutional_user.id"],
            ondelete="RESTRICT"
        ),
    )


def downgrade() -> None:
    raise NotImplementedError("Downgrade not supported.")