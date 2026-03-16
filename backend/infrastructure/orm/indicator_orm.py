import uuid
from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from backend.infrastructure.orm.base import Base


class IndicatorORM(Base):
    __tablename__ = "indicator"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    competency_id = Column(UUID(as_uuid=True), nullable=False)

    description = Column(Text, nullable=False)

    total_stages = Column(Integer, nullable=False)
    version_number = Column(Integer, nullable=False)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
