"""0001_initial_full_schema_v3

Revision ID: e8246f96ef44
Revises: None
Create Date: 2026-02-28
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision: str = 'e8246f96ef44'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    # =====================================================
    # EXTENSIONS
    # =====================================================

    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')

    # =====================================================
    # ENUM TYPES (SAFE CREATE)
    # =====================================================

    op.execute("""
    DO $$
    BEGIN
        IF NOT EXISTS (
            SELECT 1 FROM pg_type WHERE typname = 'academic_year_status'
        ) THEN
            CREATE TYPE academic_year_status AS ENUM (
                'draft',
                'active',
                'closed'
            );
        END IF;
    END
    $$;
    """)

    academic_year_status_enum = postgresql.ENUM(
        'draft',
        'active',
        'closed',
        name='academic_year_status',
        create_type=False
    )

    # =====================================================
    # CORE PEDAGOGICAL STRUCTURE
    # =====================================================

    op.create_table(
        'institution',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('identity', postgresql.JSONB(), nullable=False),
        sa.Column('governance', postgresql.JSONB(), nullable=False),
        sa.Column('pedagogical_framework', postgresql.JSONB(), nullable=False),
        sa.Column('organization_model', sa.String(20), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
    )

    op.create_table(
        'subject',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('institution_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('name', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['institution_id'], ['institution.id'], ondelete='RESTRICT'),
    )

    op.create_table(
        'nucleus',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('subject_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('name', sa.Text(), nullable=False),
        sa.Column('description', sa.Text()),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], ondelete='RESTRICT'),
    )

    op.create_table(
        'competency',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('nucleus_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['nucleus_id'], ['nucleus.id'], ondelete='RESTRICT'),
    )

    op.create_table(
        'indicator',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('competency_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('total_stages', sa.Integer(), nullable=False),
        sa.Column('version_number', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['competency_id'], ['competency.id'], ondelete='RESTRICT'),
    )

    op.create_table(
        'indicator_stage',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('indicator_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('stage_order', sa.Integer(), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('normalized_level', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['indicator_id'], ['indicator.id'], ondelete='RESTRICT'),
        sa.UniqueConstraint('indicator_id', 'stage_order', name='uq_indicator_stage_order')
    )

    op.create_table(
        'student',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('institution_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('external_code', sa.Text()),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['institution_id'], ['institution.id'], ondelete='RESTRICT'),
    )

    # =====================================================
    # ACADEMIC CONTEXT
    # =====================================================

    op.create_table(
        'academic_level',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('institution_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('order_index', sa.Integer(), nullable=False),
        sa.Column('education_stage', sa.String()),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['institution_id'], ['institution.id'], ondelete='RESTRICT'),
        sa.UniqueConstraint('institution_id', 'name', name='uq_academic_level_institution_name')
    )

    op.create_table(
        'academic_year',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('institution_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('start_date', sa.Date(), nullable=False),
        sa.Column('end_date', sa.Date(), nullable=False),
        sa.Column('status', academic_year_status_enum, nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['institution_id'], ['institution.id'], ondelete='RESTRICT'),
    )

    # =====================================================
    # ROLES
    # =====================================================

    op.create_table(
        'role',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('code', sa.String(50), nullable=False),
        sa.Column('system_name', sa.String(100), nullable=False),
        sa.Column('description', sa.Text()),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.UniqueConstraint('code', name='uq_role_code')
    )

    op.execute("""
        INSERT INTO role (id, code, system_name, description, created_at, updated_at)
        VALUES
        (uuid_generate_v4(), 'ADMIN', 'Administrador', 'Superusuario institucional', now(), now()),
        (uuid_generate_v4(), 'DIRECTOR', 'Director', 'Director institucional o de nivel', now(), now()),
        (uuid_generate_v4(), 'ACADEMIC_COORDINATOR', 'Coordinador Académico', 'Coordinador por área o institución', now(), now()),
        (uuid_generate_v4(), 'TEACHER', 'Docente', 'Docente de asignatura', now(), now()),
        (uuid_generate_v4(), 'GROUP_COORDINATOR', 'Coordinador de Grupo', 'Responsable formativo de grupo', now(), now()),
        (uuid_generate_v4(), 'PSYCHOLOGY', 'Psicología / DOA', 'Área de orientación o psicología', now(), now());
    """)


def downgrade() -> None:
    raise NotImplementedError("Downgrade not supported for initial schema.")
