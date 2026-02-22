# backend/infrastructure/orm/academic_period_orm.py

import uuid
from sqlalchemy import Column, String, Date, Boolean, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from backend.infrastructure.orm.base import Base


class AcademicPeriodORM(Base):
    __tablename__ = "academic_period"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    academic_year_id = Column(
        UUID(as_uuid=True),
        ForeignKey("academic_year.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    name = Column(String, nullable=False)

    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    is_closed = Column(
        Boolean,
        nullable=False,
        default=False,
    )

    snapshot_generated_at = Column(
        DateTime(timezone=False),
        nullable=True,
    )

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