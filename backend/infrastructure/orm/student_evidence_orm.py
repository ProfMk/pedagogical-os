import uuid
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from backend.infrastructure.orm.base import Base


class StudentEvidenceORM(Base):
    __tablename__ = "student_evidence"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    student_id = Column(
        UUID(as_uuid=True),
        ForeignKey("student.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    indicator_id = Column(
        UUID(as_uuid=True),
        ForeignKey("indicator.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    indicator_stage_id = Column(
        UUID(as_uuid=True),
        ForeignKey("indicator_stage.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    raw_score = Column(
        Integer,
        nullable=False
    )

    recorded_at = Column(
        DateTime(timezone=False),
        nullable=False
    )