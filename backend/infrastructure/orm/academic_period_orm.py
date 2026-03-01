import uuid
from sqlalchemy import Column, String, Date, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from backend.infrastructure.orm.base import Base


class AcademicPeriodORM(Base):
    __tablename__ = "academic_period"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    academic_year_id = Column(UUID(as_uuid=True), nullable=False)

    name = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    is_closed = Column(Boolean, nullable=False)
    snapshot_generated_at = Column(DateTime, nullable=True)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)