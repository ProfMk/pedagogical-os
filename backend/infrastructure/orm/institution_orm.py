import uuid
from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID, JSONB
from backend.infrastructure.orm.base import Base


class InstitutionORM(Base):
    __tablename__ = "institution"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    identity = Column(JSONB, nullable=False)
    governance = Column(JSONB, nullable=False)
    pedagogical_framework = Column(JSONB, nullable=False)

    organization_model = Column(String(20), nullable=False)

    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)