# backend/infrastructure/orm/student_enrollment_orm.py

import uuid
from sqlalchemy import Column, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from backend.infrastructure.orm.base import Base


class StudentEnrollmentORM(Base):
    __tablename__ = "student_enrollment"

    __table_args__ = (
        UniqueConstraint(
            "student_id",
            "academic_year_id",
            name="uq_student_enrollment_student_year"
        ),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    student_id = Column(
        UUID(as_uuid=True),
        ForeignKey("student.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    academic_year_id = Column(
        UUID(as_uuid=True),
        ForeignKey("academic_year.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    academic_level_id = Column(
        UUID(as_uuid=True),
        ForeignKey("academic_level.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

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