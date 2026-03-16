from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from backend.application.dto.group_student_dto import GroupStudentDTO


class StudentRepositoryPort(ABC):

    @abstractmethod
    def get_students_for_group(
        self,
        group_id: UUID
    ) -> List[GroupStudentDTO]:
        pass
