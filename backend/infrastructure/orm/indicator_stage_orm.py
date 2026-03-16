import uuid
from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from backend.infrastructure.orm.base import Base


class IndicatorStageORM(Base):
    __tablename__ = "indicator_stage"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    indicator_id = Column(UUID(as_uuid=True), nullable=False)

    stage_order = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)

    normalized_level = Column(Integer, nullable=False)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
