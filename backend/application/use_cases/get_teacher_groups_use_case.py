from typing import List
from uuid import UUID

from backend.application.dtos.teacher_group_dto import TeacherGroupDTO
from backend.application.ports.group_repository_port import GroupRepositoryPort


class GetTeacherGroupsUseCase:

    def __init__(self, repository: GroupRepositoryPort):
        self.repository = repository

    def execute(
        self,
        teacher_id: UUID
    ) -> List[TeacherGroupDTO]:
        return self.repository.get_groups_for_teacher(teacher_id)
