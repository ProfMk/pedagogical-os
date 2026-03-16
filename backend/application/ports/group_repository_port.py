from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from backend.application.dto.teacher_group_dto import TeacherGroupDTO


class GroupRepositoryPort(ABC):

    @abstractmethod
    def get_groups_for_teacher(
        self,
        teacher_id: UUID
    ) -> List[TeacherGroupDTO]:
        pass
