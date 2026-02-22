from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from backend.app.settings import settings


engine = create_engine(
    settings.database_url,
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    future=True,
)


def get_session() -> Generator[Session, None, None]:
    """
    FastAPI dependency that provides a SQLAlchemy session.
    """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
