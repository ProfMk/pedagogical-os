from uuid import UUID

from fastapi import APIRouter, Depends

from backend.application.use_cases.get_group_students_use_case import (
    GetGroupStudentsUseCase,
)
from backend.application.use_cases.get_student_indicators_use_case import (
    GetStudentIndicatorsUseCase,
)
from backend.application.use_cases.get_teacher_groups_use_case import (
    GetTeacherGroupsUseCase,
)
from backend.infrastructure.orm.session import get_session
from backend.infrastructure.repositories.group_repository import GroupRepository
from backend.infrastructure.repositories.indicator_repository import IndicatorRepository
from backend.infrastructure.repositories.student_repository import StudentRepository

router = APIRouter()


def get_teacher_groups_use_case(session=Depends(get_session)):
    repository = GroupRepository(session)
    return GetTeacherGroupsUseCase(repository)


def get_group_students_use_case(session=Depends(get_session)):
    repository = StudentRepository(session)
    return GetGroupStudentsUseCase(repository)


def get_student_indicators_use_case(session=Depends(get_session)):
    repository = IndicatorRepository(session)
    return GetStudentIndicatorsUseCase(repository)


@router.get("/groups")
def get_groups(
    teacher_id: UUID,
    institution_id: UUID,
    academic_year_id: UUID,
    use_case: GetTeacherGroupsUseCase = Depends(get_teacher_groups_use_case),
):
    return use_case.execute(
        teacher_id=teacher_id,
        institution_id=institution_id,
        academic_year_id=academic_year_id,
    )


@router.get("/groups/{group_id}/students")
def get_group_students(
    group_id: UUID,
    use_case: GetGroupStudentsUseCase = Depends(get_group_students_use_case),
):
    return use_case.execute(group_id=group_id)


@router.get("/students/{student_id}/indicators")
def get_student_indicators(
    student_id: UUID,
    use_case: GetStudentIndicatorsUseCase = Depends(get_student_indicators_use_case),
):
    return use_case.execute(student_id=student_id)
