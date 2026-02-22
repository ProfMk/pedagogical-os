# backend/infrastructure/orm/nucleus_orm.py

import uuid
from sqlalchemy import Column, DateTime, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from backend.infrastructure.orm.base import Base


class NucleusORM(Base):
    __tablename__ = "nucleus"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    subject_id = Column(
        UUID(as_uuid=True),
        ForeignKey("subject.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    name = Column(Text, nullable=False)
    description = Column(Text, nullable=True)

    created_at = Column(DateTime(timezone=False), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=False), server_default=func.now(), onupdate=func.now(), nullable=False)