from uuid import uuid4

from sqlalchemy import (
    Column,
    Integer,
    Numeric,
    DateTime,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from backend.infrastructure.orm.base import Base


class StudentIndicatorProgressORM(Base):
    """
    ORM model mapping the 'student_indicator_progress' table.

    This class:
    - knows about tables and columns
    - knows about SQLAlchemy
    - knows NOTHING about pedagogical meaning
    """

    __tablename__ = "student_indicator_progress"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    student_id = Column(
        UUID(as_uuid=True),
        ForeignKey("student.id", ondelete="RESTRICT"),
        nullable=False,
    )

    indicator_id = Column(
        UUID(as_uuid=True),
        ForeignKey("indicator.id", ondelete="RESTRICT"),
        nullable=False,
    )

    current_stage_order = Column(Integer, nullable=True)

    consolidation_score = Column(Numeric(5, 4), nullable=True)

    normalized_level_internal = Column(Numeric(5, 2), nullable=True)

    created_at = Column(
        DateTime(timezone=False),
        server_default=func.now(),
        nullable=False,
    )

    updated_at = Column(
        DateTime(timezone=False),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    __table_args__ = (
        UniqueConstraint(
            "student_id",
            "indicator_id",
            name="uq_student_indicator",
        ),
    )
