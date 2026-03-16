import uuid
from sqlalchemy import Column, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID

from backend.infrastructure.orm.base import Base


class AcademicGroupORM(Base):
    __tablename__ = "academic_group"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    academic_year_id = Column(UUID(as_uuid=True), nullable=False)
    academic_grade_id = Column(UUID(as_uuid=True), nullable=False)

    name = Column(Text, nullable=False)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
