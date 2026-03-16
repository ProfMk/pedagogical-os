import uuid
from sqlalchemy import Column, String, Date, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID
from backend.infrastructure.orm.base import Base


class AcademicYearORM(Base):
    __tablename__ = "academic_year"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    institution_id = Column(UUID(as_uuid=True), nullable=False)

    name = Column(String, nullable=False)

    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    status = Column(
        Enum("draft", "active", "closed", name="academic_year_status"),
        nullable=False,
    )

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
