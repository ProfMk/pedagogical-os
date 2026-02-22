# backend/infrastructure/orm/indicator_stage_orm.py

import uuid
from sqlalchemy import Column, DateTime, Text, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from backend.infrastructure.orm.base import Base


class IndicatorStageORM(Base):
    __tablename__ = "indicator_stage"

    __table_args__ = (
        UniqueConstraint("indicator_id", "stage_order", name="uq_indicator_stage_order"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    indicator_id = Column(
        UUID(as_uuid=True),
        ForeignKey("indicator.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    stage_order = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    normalized_level = Column(Integer, nullable=False)

    created_at = Column(DateTime(timezone=False), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=False), server_default=func.now(), onupdate=func.now(), nullable=False)