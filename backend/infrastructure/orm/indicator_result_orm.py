from sqlalchemy import Column, ForeignKey, Numeric, Boolean, Text, DateTime, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from backend.infrastructure.orm.base import Base


class IndicatorResultORM(Base):
    __tablename__ = "indicator_result"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.uuid_generate_v4())

    student_id = Column(
        UUID(as_uuid=True),
        ForeignKey("student.id", ondelete="RESTRICT"),
        nullable=False
    )

    indicator_id = Column(
        UUID(as_uuid=True),
        ForeignKey("indicator.id", ondelete="RESTRICT"),
        nullable=False
    )

    calculated_level = Column(Numeric(5, 2), nullable=False)

    final_level = Column(Numeric(5, 2), nullable=False)

    override_flag = Column(Boolean, nullable=False, default=False)

    override_comment = Column(Text, nullable=True)

    created_at = Column(DateTime, nullable=False, server_default=func.now())

    updated_at = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now())

    __table_args__ = (
        UniqueConstraint("student_id", "indicator_id", name="uq_indicator_result_student_indicator"),
    )