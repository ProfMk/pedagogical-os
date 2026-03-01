import uuid
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID
from backend.infrastructure.orm.base import Base


class StudentEvidenceORM(Base):
    __tablename__ = "student_evidence"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    academic_year_id = Column(UUID(as_uuid=True), nullable=False)
    student_id = Column(UUID(as_uuid=True), nullable=False)
    indicator_id = Column(UUID(as_uuid=True), nullable=False)
    indicator_stage_id = Column(UUID(as_uuid=True), nullable=False)

    raw_score = Column(Integer, nullable=False)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)