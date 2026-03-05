import pytest
import pkgutil
import importlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.infrastructure.orm.base import Base
import backend.infrastructure.orm as orm_package

# import fixture so pytest discovers it
from backend.tests.fixtures.academic_context import academic_context


TEST_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/pedagogical_os_test"


def import_all_orm_models():
    for _, module_name, _ in pkgutil.iter_modules(orm_package.__path__):
        if module_name.endswith("_orm"):
            importlib.import_module(f"{orm_package.__name__}.{module_name}")


@pytest.fixture(scope="session")
def engine():

    import_all_orm_models()

    engine = create_engine(TEST_DATABASE_URL)

    Base.metadata.create_all(engine)

    yield engine

    Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def test_db_session(engine):
    connection = engine.connect()
    transaction = connection.begin()

    SessionLocal = sessionmaker(bind=connection)
    session = SessionLocal()

    yield session

    session.close()
    transaction.rollback()
    connection.close()