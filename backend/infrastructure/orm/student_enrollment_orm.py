import uuid
from sqlalchemy import Column, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from backend.infrastructure.orm.base import Base


class StudentEnrollmentORM(Base):
    __tablename__ = "student_enrollment"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    academic_year_id = Column(UUID(as_uuid=True), nullable=False)
    student_id = Column(UUID(as_uuid=True), nullable=False)
    academic_group_id = Column(UUID(as_uuid=True), nullable=False)

    enrolled_at = Column(DateTime, nullable=False)
    withdrawn_at = Column(DateTime, nullable=True)

    is_active = Column(Boolean, nullable=False)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)