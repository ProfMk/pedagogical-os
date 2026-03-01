import uuid
from sqlalchemy import Column, Integer, DateTime, Numeric
from sqlalchemy.dialects.postgresql import UUID
from backend.infrastructure.orm.base import Base


class StudentIndicatorProgressORM(Base):
    __tablename__ = "student_indicator_progress"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    academic_year_id = Column(UUID(as_uuid=True), nullable=False)
    student_id = Column(UUID(as_uuid=True), nullable=False)
    indicator_id = Column(UUID(as_uuid=True), nullable=False)

    current_stage_order = Column(Integer, nullable=False)

    consolidation_score = Column(Numeric(5, 4), nullable=True)
    normalized_level_internal = Column(Numeric(5, 2), nullable=True)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)