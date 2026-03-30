from dataclasses import asdict
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from backend.application.use_cases.get_teacher_group_progress_tree_use_case import (
    GetTeacherGroupProgressTreeUseCase,
)
from backend.infrastructure.orm.session import get_session
from backend.infrastructure.repositories.teacher_group_progress_repository import (
    TeacherGroupProgressRepository,
)

router = APIRouter()


def _parse_uuid(value: str, field_name: str) -> UUID:
    try:
        return UUID(value)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=f"Invalid UUID: {field_name}") from error


def get_use_case(session=Depends(get_session)) -> GetTeacherGroupProgressTreeUseCase:
    repository = TeacherGroupProgressRepository(session)
    return GetTeacherGroupProgressTreeUseCase(repository)


@router.get("/teacher/group-indicator-tree")
def get_group_indicator_tree(
    institution_id: str,
    academic_year_id: str,
    teacher_id: str,
    subject_id: str,
    group_id: str,
    use_case: GetTeacherGroupProgressTreeUseCase = Depends(get_use_case),
) -> dict:
    institution_uuid = _parse_uuid(institution_id, "institution_id")
    academic_year_uuid = _parse_uuid(academic_year_id, "academic_year_id")
    teacher_uuid = _parse_uuid(teacher_id, "teacher_id")
    subject_uuid = _parse_uuid(subject_id, "subject_id")
    group_uuid = _parse_uuid(group_id, "group_id")

    response = use_case.execute(
        institution_id=institution_uuid,
        academic_year_id=academic_year_uuid,
        teacher_id=teacher_uuid,
        subject_id=subject_uuid,
        group_id=group_uuid,
    )

    return asdict(response)
