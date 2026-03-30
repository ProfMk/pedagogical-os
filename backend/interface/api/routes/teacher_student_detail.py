from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.application.dto.student_detail_dto import StudentDetailDTO
from backend.application.use_cases.get_student_detail_use_case import (
    GetStudentDetailUseCase,
)
from backend.infrastructure.orm.session import get_session
from backend.infrastructure.repositories.student_detail_repository_impl import (
    StudentDetailRepositoryImpl,
)

router = APIRouter()


def get_use_case(session: Session = Depends(get_session)) -> GetStudentDetailUseCase:
    repository = StudentDetailRepositoryImpl(session)
    return GetStudentDetailUseCase(repository)


@router.get("/teacher/student-detail", response_model=StudentDetailDTO)
def get_student_detail(
    institution_id: UUID,
    academic_year_id: UUID,
    student_id: UUID,
    use_case: GetStudentDetailUseCase = Depends(get_use_case),
) -> StudentDetailDTO:
    try:
        return use_case.execute(
            institution_id=institution_id,
            academic_year_id=academic_year_id,
            student_id=student_id,
        )
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error)) from error
