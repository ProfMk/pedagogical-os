import pathlib
import pytest


def load_sql_file(session, filepath: str):
    """
    Executes a SQL seed file inside the provided SQLAlchemy session.
    """

    sql_path = pathlib.Path(filepath)

    if not sql_path.exists():
        raise FileNotFoundError(f"Seed file not found: {filepath}")

    sql = sql_path.read_text()

    session.execute(sql)
    session.commit()


@pytest.fixture
def real_school_dataset(test_db_session):
    """
    Loads a realistic school dataset for simulation tests.

    Dataset includes:
    - subjects
    - grades
    - groups
    - ~120 students
    - curriculum
    - indicators
    - stages
    - ~5000 evidence records
    """

    seed_file = "backend/tests/seeds/seed_real_school.sql"

    load_sql_file(test_db_session, seed_file)

    return test_db_session
