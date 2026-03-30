from typing import List, Protocol
from uuid import UUID


class TeacherGroupProgressRepositoryPort(Protocol):

    def get_group_progress_tree(
        self,
        institution_id: UUID,
        academic_year_id: UUID,
        teacher_id: UUID,
        subject_id: UUID,
        group_id: UUID,
    ) -> List[dict]:
        ...
