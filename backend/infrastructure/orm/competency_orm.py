# backend/infrastructure/orm/competency_orm.py

import uuid
from sqlalchemy import Column, DateTime, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from backend.infrastructure.orm.base import Base


class CompetencyORM(Base):
    __tablename__ = "competency"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    nucleus_id = Column(
        UUID(as_uuid=True),
        ForeignKey("nucleus.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    description = Column(Text, nullable=False)

    created_at = Column(DateTime(timezone=False), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=False), server_default=func.now(), onupdate=func.now(), nullable=False)