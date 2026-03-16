import uuid
from sqlalchemy import Column, DateTime, Boolean, Text, Numeric
from sqlalchemy.dialects.postgresql import UUID
from backend.infrastructure.orm.base import Base


class IndicatorResultORM(Base):
    __tablename__ = "indicator_result"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    academic_year_id = Column(UUID(as_uuid=True), nullable=False)
    academic_period_id = Column(UUID(as_uuid=True), nullable=False)
    student_id = Column(UUID(as_uuid=True), nullable=False)
    indicator_id = Column(UUID(as_uuid=True), nullable=False)

    calculated_level = Column(Numeric(5, 2), nullable=False)
    final_level = Column(Numeric(5, 2), nullable=False)

    override_flag = Column(Boolean, nullable=False)
    override_comment = Column(Text, nullable=True)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
