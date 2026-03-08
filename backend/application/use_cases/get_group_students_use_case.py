from typing import List
from uuid import UUID

from backend.application.dtos.group_student_dto import GroupStudentDTO
from backend.infrastructure.repositories.student_repository import StudentRepository


class GetGroupStudentsUseCase:

    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def execute(
        self,
        group_id: UUID
    ) -> List[GroupStudentDTO]:
        return self.repository.get_students_for_group(group_id)
