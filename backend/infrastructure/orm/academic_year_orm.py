# backend/infrastructure/orm/academic_year_orm.py

import uuid
from sqlalchemy import Column, String, Date, Enum, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from backend.infrastructure.orm.base import Base


class AcademicYearORM(Base):
    __tablename__ = "academic_year"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    institution_id = Column(
        UUID(as_uuid=True),
        ForeignKey("institution.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    name = Column(String, nullable=False)

    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    status = Column(
        Enum("draft", "active", "closed", name="academic_year_status"),
        nullable=False,
        default="draft",
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