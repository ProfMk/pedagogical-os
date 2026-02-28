"""0002_complete_operational_structure

Revision ID: f3c378d9e15b
Revises: e8246f96ef44
Create Date: 2026-02-28
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision: str = 'f3c378d9e15b'
down_revision: Union[str, Sequence[str], None] = 'e8246f96ef44'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    # =====================================================
    # ACADEMIC PERIOD
    # =====================================================

    op.create_table(
        'academic_period',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('academic_year_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('start_date', sa.Date(), nullable=False),
        sa.Column('end_date', sa.Date(), nullable=False),
        sa.Column('is_closed', sa.Boolean(), nullable=False),
        sa.Column('snapshot_generated_at', sa.DateTime()),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['academic_year_id'], ['academic_year.id']),
    )

    # =====================================================
    # GRADES & GROUPS
    # =====================================================

    op.create_table(
        'academic_grade',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('institution_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('academic_level_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('order_index', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['institution_id'], ['institution.id']),
        sa.ForeignKeyConstraint(['academic_level_id'], ['academic_level.id']),
        sa.UniqueConstraint('institution_id', 'academic_level_id', 'name',
                            name='uq_academic_grade_per_level')
    )

    op.create_table(
        'academic_group',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('academic_year_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('academic_grade_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['academic_year_id'], ['academic_year.id']),
        sa.ForeignKeyConstraint(['academic_grade_id'], ['academic_grade.id']),
        sa.UniqueConstraint('academic_year_id', 'academic_grade_id', 'name',
                            name='uq_academic_group_per_year')
    )

    # =====================================================
    # STUDENT ENROLLMENT
    # =====================================================

    op.create_table(
        'student_enrollment',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('academic_year_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('student_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('academic_group_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('enrolled_at', sa.DateTime(), nullable=False),
        sa.Column('withdrawn_at', sa.DateTime()),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['academic_year_id'], ['academic_year.id']),
        sa.ForeignKeyConstraint(['student_id'], ['student.id']),
        sa.ForeignKeyConstraint(['academic_group_id'], ['academic_group.id']),
    )

    # =====================================================
    # ANNUALIZED PROGRESS
    # =====================================================

    op.create_table(
        'student_indicator_progress',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('academic_year_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('student_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('indicator_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('current_stage_order', sa.Integer(), nullable=False),
        sa.Column('consolidation_score', sa.Numeric(5, 4)),
        sa.Column('normalized_level_internal', sa.Numeric(5, 2)),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['academic_year_id'], ['academic_year.id']),
        sa.ForeignKeyConstraint(['student_id'], ['student.id']),
        sa.ForeignKeyConstraint(['indicator_id'], ['indicator.id']),
        sa.UniqueConstraint('student_id', 'indicator_id', 'academic_year_id',
                            name='uq_student_indicator_year')
    )

    op.create_table(
        'student_evidence',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('academic_year_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('student_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('indicator_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('indicator_stage_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('raw_score', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['academic_year_id'], ['academic_year.id']),
        sa.ForeignKeyConstraint(['student_id'], ['student.id']),
        sa.ForeignKeyConstraint(['indicator_id'], ['indicator.id']),
        sa.ForeignKeyConstraint(['indicator_stage_id'], ['indicator_stage.id']),
    )

    op.create_table(
        'indicator_result',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('academic_year_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('student_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('indicator_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('calculated_level', sa.Numeric(5, 2), nullable=False),
        sa.Column('final_level', sa.Numeric(5, 2), nullable=False),
        sa.Column('override_flag', sa.Boolean(), nullable=False),
        sa.Column('override_comment', sa.Text()),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['academic_year_id'], ['academic_year.id']),
        sa.ForeignKeyConstraint(['student_id'], ['student.id']),
        sa.ForeignKeyConstraint(['indicator_id'], ['indicator.id']),
        sa.UniqueConstraint('student_id', 'indicator_id', 'academic_year_id',
                            name='uq_indicator_result_per_year')
    )

    # =====================================================
    # IDENTITY
    # =====================================================

    op.create_table(
        'institutional_user',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('institution_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('password_hash', sa.Text(), nullable=False),
        sa.Column('full_name', sa.String(255), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('is_superadmin', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['institution_id'], ['institution.id']),
        sa.UniqueConstraint('institution_id', 'email',
                            name='uq_user_email_per_institution')
    )


def downgrade() -> None:
    raise NotImplementedError("Downgrade not supported.")