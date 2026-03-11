from uuid import UUID

from fastapi import APIRouter, Depends, Header

from backend.application.use_cases.get_teacher_dashboard_use_case import (
    GetTeacherDashboardUseCase,
)
from backend.infrastructure.orm.session import get_session
from backend.infrastructure.repositories.dashboard_repository import DashboardRepository

router = APIRouter()


class TeacherContext:
    def __init__(self, institution_id: UUID, academic_year_id: UUID):
        self.institution_id = institution_id
        self.academic_year_id = academic_year_id


def get_authenticated_teacher_context(
    x_institution_id: UUID = Header(alias="X-Institution-Id"),
    x_academic_year_id: UUID = Header(alias="X-Academic-Year-Id"),
) -> TeacherContext:
    return TeacherContext(
        institution_id=x_institution_id,
        academic_year_id=x_academic_year_id,
    )


def get_use_case(session=Depends(get_session)):
    repository = DashboardRepository(session)
    return GetTeacherDashboardUseCase(repository)


@router.get("/teacher/dashboard")
def get_teacher_dashboard(
    context: TeacherContext = Depends(get_authenticated_teacher_context),
    use_case: GetTeacherDashboardUseCase = Depends(get_use_case),
):
    dto = use_case.execute(
        institution_id=context.institution_id,
        academic_year_id=context.academic_year_id,
    )
    return dto.model_dump()
