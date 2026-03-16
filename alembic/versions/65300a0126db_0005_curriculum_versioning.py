"""0005_curriculum_versioning

Revision ID: 65300a0126db
Revises: 2f5bd810d55e
Create Date: 2026-02-28
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision: str = "65300a0126db"
down_revision: Union[str, Sequence[str], None] = "2f5bd810d55e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    # ------------------------------------------------------------
    # 1️⃣ Create ENUM safely (idempotent)
    # ------------------------------------------------------------

    op.execute(
        """
        DO $$
        BEGIN
            IF NOT EXISTS (
                SELECT 1 FROM pg_type WHERE typname = 'curriculum_version_status'
            ) THEN
                CREATE TYPE curriculum_version_status AS ENUM (
                    'draft',
                    'active',
                    'locked'
                );
            END IF;
        END
        $$;
        """
    )

    curriculum_status_enum = postgresql.ENUM(
        "draft",
        "active",
        "locked",
        name="curriculum_version_status",
        create_type=False
    )

    # ------------------------------------------------------------
    # 2️⃣ Create curriculum_version table
    # ------------------------------------------------------------

    op.create_table(
        "curriculum_version",

        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),

        sa.Column("institution_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("academic_year_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("academic_level_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("academic_grade_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("subject_id", postgresql.UUID(as_uuid=True), nullable=False),

        sa.Column("version_number", sa.Integer(), nullable=False),

        sa.Column(
            "status",
            curriculum_status_enum,
            nullable=False,
            server_default=sa.text("'draft'")
        ),

        sa.Column(
            "parent_version_id",
            postgresql.UUID(as_uuid=True),
            nullable=True,
        ),

        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),

        sa.ForeignKeyConstraint(
            ["institution_id"],
            ["institution.id"],
            ondelete="CASCADE",
        ),

        sa.ForeignKeyConstraint(
            ["academic_year_id"],
            ["academic_year.id"],
            ondelete="CASCADE",
        ),

        sa.ForeignKeyConstraint(
            ["academic_level_id"],
            ["academic_level.id"],
            ondelete="RESTRICT",
        ),

        sa.ForeignKeyConstraint(
            ["academic_grade_id"],
            ["academic_grade.id"],
            ondelete="RESTRICT",
        ),

        sa.ForeignKeyConstraint(
            ["subject_id"],
            ["subject.id"],
            ondelete="RESTRICT",
        ),

        sa.ForeignKeyConstraint(
            ["parent_version_id"],
            ["curriculum_version.id"],
            ondelete="SET NULL",
        ),

        sa.UniqueConstraint(
            "academic_year_id",
            "academic_level_id",
            "academic_grade_id",
            "subject_id",
            name="uq_curriculum_version_per_scope",
        ),
    )

    # ------------------------------------------------------------
    # 3️⃣ Index for performance
    # ------------------------------------------------------------

    op.create_index(
        "ix_curriculum_version_scope",
        "curriculum_version",
        [
            "institution_id",
            "academic_year_id",
            "academic_grade_id",
            "subject_id",
        ],
    )

    # ------------------------------------------------------------
    # 4️⃣ Modify nucleus structure
    # ------------------------------------------------------------

    # Add curriculum_version_id column (nullable temporarily)
    op.add_column(
        "nucleus",
        sa.Column(
            "curriculum_version_id",
            postgresql.UUID(as_uuid=True),
            nullable=True,
        ),
    )

    # Create FK to curriculum_version
    op.create_foreign_key(
        "fk_nucleus_curriculum_version",
        "nucleus",
        "curriculum_version",
        ["curriculum_version_id"],
        ["id"],
        ondelete="CASCADE",
    )

    # Drop subject_id column (FK will be dropped automatically)
    op.drop_column("nucleus", "subject_id")

    # Make curriculum_version_id NOT NULL
    op.alter_column(
        "nucleus",
        "curriculum_version_id",
        nullable=False,
    )


def downgrade() -> None:
    raise NotImplementedError("Downgrade not supported.")
