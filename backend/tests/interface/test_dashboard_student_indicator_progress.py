from uuid import uuid4

from fastapi import FastAPI
from fastapi.testclient import TestClient

from backend.interface.api.dashboard import router
from backend.infrastructure.orm.session import get_session
from backend.infrastructure.orm.indicator_orm import IndicatorORM
from backend.application.dto.student_indicator_progress_read_dto import (
    StudentIndicatorProgressReadDTO
)
from backend.application.use_cases.get_student_indicator_progress import (
    GetStudentIndicatorProgressUseCase
)


# --- Fake session dependency (NO DB access) ------------------

def fake_get_session():
    class FakeSession:
        def get(self, model, obj_id):
            # Simula que el indicador SÍ existe
            if model is IndicatorORM:
                return IndicatorORM(
                    id=obj_id,
                    description="Resuelve sumas con llevadas",
                    total_stages=4,
                )
            return None

    yield FakeSession()


# --- Test app ------------------------------------------------

def create_test_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)

    # Override real DB session with fake one
    app.dependency_overrides[get_session] = fake_get_session

    return app


# --- Test ----------------------------------------------------

def test_dashboard_indicator_student_progress_with_low_consolidation_alert(monkeypatch):
    """
    GIVEN a student with consolidation < 0.60
    WHEN the individual dashboard endpoint is called
    THEN a low consolidation alert is returned
    """

    # --- Arrange ---
    app = create_test_app()
    client = TestClient(app)

    student_id = uuid4()
    indicator_id = uuid4()

    fake_dto = StudentIndicatorProgressReadDTO(
        student_id=student_id,
        student_name="Juan Pérez",

        indicator_id=indicator_id,
        indicator_description="Resuelve sumas con llevadas",

        current_stage=2,
        total_stages=4,

        normalized_level_internal=2.3,
        consolidation_score=0.45,

        has_low_consolidation_alert=True
    )

    def fake_execute(*args, **kwargs):
        return fake_dto

    # Mock ONLY the use case execution
    monkeypatch.setattr(
        GetStudentIndicatorProgressUseCase,
        "execute",
        fake_execute
    )

    # --- Act ---
    response = client.get(
        f"/dashboard/indicator/{indicator_id}/student/{student_id}"
    )

    # --- Assert ---
    assert response.status_code == 200

    data = response.json()

    assert data["studentName"] == "Juan Pérez"
    assert data["currentStage"] == 2
    assert data["totalStages"] == 4
    assert data["consolidationScore"] == 0.45
    assert data["hasLowConsolidationAlert"] is True
