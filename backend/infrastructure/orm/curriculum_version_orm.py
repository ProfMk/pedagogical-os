import uuid
from sqlalchemy import Column, Integer, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID
from backend.infrastructure.orm.base import Base


class CurriculumVersionORM(Base):
    __tablename__ = "curriculum_version"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    institution_id = Column(UUID(as_uuid=True), nullable=False)
    academic_year_id = Column(UUID(as_uuid=True), nullable=False)
    academic_level_id = Column(UUID(as_uuid=True), nullable=False)
    academic_grade_id = Column(UUID(as_uuid=True), nullable=False)
    subject_id = Column(UUID(as_uuid=True), nullable=False)

    version_number = Column(Integer, nullable=False)

    status = Column(
        Enum("draft", "active", "locked", name="curriculum_version_status"),
        nullable=False,
    )

    parent_version_id = Column(UUID(as_uuid=True), nullable=True)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
