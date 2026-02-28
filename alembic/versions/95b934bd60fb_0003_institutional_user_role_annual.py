"""0003_institutional_user_role_annual

Revision ID: 95b934bd60fb
Revises: f3c378d9e15b
Create Date: 2026-02-28
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision: str = '95b934bd60fb'
down_revision: Union[str, Sequence[str], None] = 'f3c378d9e15b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.create_table(
        'institutional_user_role',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),

        sa.Column('academic_year_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('institutional_user_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('role_id', postgresql.UUID(as_uuid=True), nullable=False),

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
            ['role_id'],
            ['role.id'],
            ondelete='RESTRICT'
        ),

        sa.UniqueConstraint(
            'academic_year_id',
            'institutional_user_id',
            'role_id',
            name='uq_user_role_per_year'
        )
    )


def downgrade() -> None:
    raise NotImplementedError("Downgrade not supported.")