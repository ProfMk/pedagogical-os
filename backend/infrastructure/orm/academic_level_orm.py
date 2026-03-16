import uuid
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID
from backend.infrastructure.orm.base import Base


class AcademicLevelORM(Base):
    __tablename__ = "academic_level"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    institution_id = Column(UUID(as_uuid=True), nullable=False)

    name = Column(String, nullable=False)
    order_index = Column(Integer, nullable=False)
    education_stage = Column(String, nullable=True)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
