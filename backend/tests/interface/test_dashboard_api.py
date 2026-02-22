from uuid import uuid4

from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from backend.interface.api.dashboard import router
from backend.infrastructure.orm.session import get_session


# --- Fake session dependency (NO DB access) ------------------

def fake_get_session():
    class FakeSession:
        def get(self, *args, **kwargs):
            return None  # Simula "indicator not found"

    yield FakeSession()


# --- Test app ------------------------------------------------

def create_test_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)

    # Override real DB session with fake one
    app.dependency_overrides[get_session] = fake_get_session

    return app


# --- Test ----------------------------------------------------

def test_dashboard_indicator_group_endpoint_returns_404_without_db():
    app = create_test_app()
    client = TestClient(app)

    indicator_id = uuid4()
    group_id = "1A"

    response = client.get(
        f"/dashboard/indicator/{indicator_id}/group/{group_id}"
    )

    assert response.status_code == 404
