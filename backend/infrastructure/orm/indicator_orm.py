from uuid import uuid4

from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    ForeignKey,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from backend.infrastructure.orm.base import Base


class IndicatorORM(Base):
    """
    ORM model mapping the 'indicator' table.

    This class:
    - represents an indicator row in the database
    - contains NO business logic
    - is used only for data access
    """

    __tablename__ = "indicator"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    competency_id = Column(
        UUID(as_uuid=True),
        ForeignKey("competency.id", ondelete="RESTRICT"),
        nullable=False,
    )

    description = Column(Text, nullable=False)

    total_stages = Column(Integer, nullable=False)

    version_number = Column(Integer, nullable=False)

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
