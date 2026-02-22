# backend/infrastructure/orm/academic_level_orm.py

import uuid
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from backend.infrastructure.orm.base import Base


class AcademicLevelORM(Base):
    __tablename__ = "academic_level"

    __table_args__ = (
        UniqueConstraint("institution_id", "name", name="uq_academic_level_institution_name"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    institution_id = Column(
        UUID(as_uuid=True),
        ForeignKey("institution.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    name = Column(String, nullable=False)

    order_index = Column(Integer, nullable=False)

    education_stage = Column(String, nullable=True)

    created_at = Column(
        DateTime(timezone=False),
        server_default=func.now(),
        nullable=False,
    )

    updated_at = Column(
        DateTime(timezone=False),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )