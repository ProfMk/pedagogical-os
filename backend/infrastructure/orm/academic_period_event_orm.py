from sqlalchemy import Column, ForeignKey, Text, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from backend.infrastructure.orm.base import Base

# IMPORTANT: ensure institutional_user table is registered
from backend.infrastructure.orm.institutional_user_orm import InstitutionalUserORM  # noqa


academic_period_event_type = Enum(
    "PERIOD_CLOSED",
    "PERIOD_REOPENED",
    name="academic_period_event_type",
)


class AcademicPeriodEventORM(Base):

    __tablename__ = "academic_period_event"

    id = Column(UUID(as_uuid=True), primary_key=True)

    academic_period_id = Column(
        UUID(as_uuid=True),
        ForeignKey("academic_period.id", ondelete="CASCADE"),
        nullable=False,
    )

    event_type = Column(
        academic_period_event_type,
        nullable=False,
    )

    reason = Column(
        Text,
        nullable=False,
    )

    performed_by_user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("institutional_user.id", ondelete="RESTRICT"),
        nullable=False,
    )

    created_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now(),
    )
