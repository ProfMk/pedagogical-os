import uuid
from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func

from backend.infrastructure.orm.base import Base


class InstitutionORM(Base):
    __tablename__ = "institution"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    identity = Column(JSONB, nullable=False)
    governance = Column(JSONB, nullable=False)
    pedagogical_framework = Column(JSONB, nullable=False)

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