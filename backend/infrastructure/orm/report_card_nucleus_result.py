from sqlalchemy import Column, ForeignKey, Numeric, Text, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from backend.infrastructure.orm.base import Base


class ReportCardNucleusResult(Base):
    __tablename__ = "report_card_nucleus_result"

    id = Column(UUID(as_uuid=True), primary_key=True)

    student_id = Column(
        UUID(as_uuid=True),
        ForeignKey("student.id", ondelete="CASCADE"),
        nullable=False,
    )

    subject_id = Column(
        UUID(as_uuid=True),
        ForeignKey("subject.id", ondelete="RESTRICT"),
        nullable=False,
    )

    nucleus_id = Column(
        UUID(as_uuid=True),
        ForeignKey("nucleus.id", ondelete="RESTRICT"),
        nullable=False,
    )

    academic_period_id = Column(
        UUID(as_uuid=True),
        ForeignKey("academic_period.id", ondelete="CASCADE"),
        nullable=False,
    )

    calculated_grade = Column(
        Numeric(5, 2),
        nullable=True,
    )

    final_grade = Column(
        Numeric(5, 2),
        nullable=True,
    )

    teacher_observation = Column(
        Text,
        nullable=True,
    )

    override_flag = Column(
        Boolean,
        nullable=False,
    )

    created_at = Column(
        DateTime,
        nullable=False,
    )

    updated_at = Column(
        DateTime,
        nullable=False,
    )

    # Optional relationships (no business logic)
student = relationship("StudentORM", lazy="joined")
subject = relationship("SubjectORM", lazy="joined")
nucleus = relationship("NucleusORM", lazy="joined")
