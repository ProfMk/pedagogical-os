from uuid import UUID
from typing import List

from backend.application.dto.teacher_group_dto import TeacherGroupDTO
from backend.application.ports.group_repository_port import GroupRepositoryPort


class GetTeacherGroupsUseCase:
    def __init__(self, repository: GroupRepositoryPort):
        self.repository = repository

    def execute(
        self,
        institution_id: UUID,
        academic_year_id: UUID,
        teacher_id: UUID,
    ) -> List[TeacherGroupDTO]:
        return self.repository.get_groups_for_teacher(
            institution_id=institution_id,
            academic_year_id=academic_year_id,
            teacher_id=teacher_id,
        )