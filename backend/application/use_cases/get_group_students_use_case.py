from typing import List
from uuid import UUID

from backend.application.dtos.group_student_dto import GroupStudentDTO
from backend.application.ports.student_repository_port import StudentRepositoryPort

class GetGroupStudentsUseCase:

    def __init__(self, repository: StudentRepositoryPort):
        self.repository = repository

    def execute(
        self,
        group_id: UUID
    ) -> List[GroupStudentDTO]:
        return self.repository.get_students_for_group(group_id)
