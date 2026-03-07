from fastapi.testclient import TestClient
from backend.app.main import app


client = TestClient(app)


def test_dashboard_student_progress_endpoint():

    response = client.get(
        "/dashboard/student-progress",
        params={
            "student_id": "00000000-0000-0000-0000-000000000001",
            "academic_year_id": "00000000-0000-0000-0000-000000000002"
        }
    )

    assert response.status_code in [200, 404]