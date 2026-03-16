import uuid
from sqlalchemy import Column, Text, DateTime
from sqlalchemy.dialects.postgresql import UUID
from backend.infrastructure.orm.base import Base


class CompetencyORM(Base):
    __tablename__ = "competency"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    nucleus_id = Column(UUID(as_uuid=True), nullable=False)

    description = Column(Text, nullable=False)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
