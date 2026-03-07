from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from backend.infrastructure.orm.base import Base


class InstitutionalUserORM(Base):

    __tablename__ = "institutional_user"

    id = Column(UUID(as_uuid=True), primary_key=True)

    email = Column(String, nullable=False)

    role = Column(String, nullable=False)