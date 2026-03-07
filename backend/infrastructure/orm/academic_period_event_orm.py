import uuid

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID

from backend.infrastructure.orm.base import Base


academic_period_event_type_enum = Enum(
    "PERIOD_CLOSED",
    "PERIOD_REOPENED",
    name="academic_period_event_type",
)


class AcademicPeriodEventORM(Base):
    __tablename__ = "academic_period_event"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    academic_period_id = Column(
        UUID(as_uuid=True),
        ForeignKey("academic_period.id", ondelete="CASCADE"),
        nullable=False,
    )
    event_type = Column(academic_period_event_type_enum, nullable=False)
    reason = Column(Text, nullable=False)
    performed_by_user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("institutional_user.id", ondelete="RESTRICT"),
        nullable=False,
    )
    created_at = Column(DateTime, nullable=False)
