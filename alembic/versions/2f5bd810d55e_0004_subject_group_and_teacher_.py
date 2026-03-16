"""0004_subject_group_and_teacher_assignment

Revision ID: 2f5bd810d55e
Revises: 95b934bd60fb
Create Date: 2026-02-28
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision: str = '2f5bd810d55e'
down_revision: Union[str, Sequence[str], None] = '95b934bd60fb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    # =====================================================
    # SUBJECT GROUP (Flexible Layer)
    # =====================================================

    op.create_table(
        'subject_group',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),

        sa.Column('academic_year_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('subject_id', postgresql.UUID(as_uuid=True), nullable=False),

        # Optional link for traditional / hybrid model
        sa.Column('academic_group_id', postgresql.UUID(as_uuid=True), nullable=True),

        sa.Column('name', sa.String(100), nullable=False),

        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),

        sa.ForeignKeyConstraint(
            ['academic_year_id'],
            ['academic_year.id'],
            ondelete='CASCADE'
        ),

        sa.ForeignKeyConstraint(
            ['subject_id'],
            ['subject.id'],
            ondelete='RESTRICT'
        ),

        sa.ForeignKeyConstraint(
            ['academic_group_id'],
            ['academic_group.id'],
            ondelete='SET NULL'
        ),

        sa.UniqueConstraint(
            'academic_year_id',
            'subject_id',
            'name',
            name='uq_subject_group_per_year'
        )
    )

    # =====================================================
    # TEACHER SUBJECT ASSIGNMENT
    # =====================================================

    op.create_table(
        'teacher_subject_assignment',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),

        sa.Column('academic_year_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('institutional_user_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('subject_group_id', postgresql.UUID(as_uuid=True), nullable=False),

        sa.Column('is_active', sa.Boolean(), nullable=False),

        sa.Column('assigned_at', sa.DateTime(), nullable=False),
        sa.Column('revoked_at', sa.DateTime()),

        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),

        sa.ForeignKeyConstraint(
            ['academic_year_id'],
            ['academic_year.id'],
            ondelete='CASCADE'
        ),

        sa.ForeignKeyConstraint(
            ['institutional_user_id'],
            ['institutional_user.id'],
            ondelete='CASCADE'
        ),

        sa.ForeignKeyConstraint(
            ['subject_group_id'],
            ['subject_group.id'],
            ondelete='CASCADE'
        ),

        sa.UniqueConstraint(
            'academic_year_id',
            'institutional_user_id',
            'subject_group_id',
            name='uq_teacher_subject_group'
        )
    )


def downgrade() -> None:
    raise NotImplementedError("Downgrade not supported.")
