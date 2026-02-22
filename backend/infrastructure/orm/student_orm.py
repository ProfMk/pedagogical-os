from uuid import uuid4

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from backend.infrastructure.orm.base import Base


class StudentORM(Base):
    """
    ORM model mapping the 'student' table.

    This class:
    - represents a student row in the database
    - contains NO business logic
    - exists only for persistence and joins
    """

    __tablename__ = "student"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    institution_id = Column(
        UUID(as_uuid=True),
        ForeignKey("institution.id", ondelete="RESTRICT"),
        nullable=False,
    )

    external_code = Column(Text, nullable=True)

    group_id = Column(Text, nullable=True)

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
