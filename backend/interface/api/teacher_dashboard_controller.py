from uuid import UUID

from fastapi import APIRouter, Depends

from backend.application.dto.teacher_dashboard_dto import TeacherDashboardResponse
from backend.application.use_cases.get_teacher_dashboard_use_case import (
    GetTeacherDashboardUseCase,
)
from backend.application.use_cases.get_teacher_dashboard_full_year_use_case import (
    GetTeacherDashboardFullYearUseCase,
)
from backend.infrastructure.repositories.dashboard_repository import DashboardRepository
from backend.infrastructure.orm.session import get_session

router = APIRouter()


def get_dashboard_repository():
    db = next(get_session())
    return DashboardRepository(db)


@router.get("/teacher/dashboard", response_model=TeacherDashboardResponse)
def get_teacher_dashboard(
    institution_id: UUID,
    academic_year_id: UUID,
    teacher_id: UUID,
    repository: DashboardRepository = Depends(get_dashboard_repository),
):
    use_case = GetTeacherDashboardUseCase(repository)

    return use_case.execute(
        institution_id=institution_id,
        academic_year_id=academic_year_id,
        institutional_user_id=teacher_id,
    )

@router.get("/teacher/dashboard-full-year", response_model=TeacherDashboardResponse)
def get_teacher_dashboard_full_year(
    institution_id: UUID,
    academic_year_id: UUID,
    teacher_id: UUID,
    repository: DashboardRepository = Depends(get_dashboard_repository),
):
    use_case = GetTeacherDashboardFullYearUseCase(repository)

    return use_case.execute(
        institution_id=institution_id,
        academic_year_id=academic_year_id,
        teacher_id=teacher_id,
    )