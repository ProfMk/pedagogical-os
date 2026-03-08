from typing import List
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.orm import Session

from backend.application.dtos.teacher_group_dto import TeacherGroupDTO
from backend.application.ports.group_repository_port import GroupRepositoryPort


class GroupRepository(GroupRepositoryPort):

    def __init__(self, session: Session):
        self.session = session

    def get_groups_for_teacher(
        self,
        teacher_id: UUID
    ) -> List[TeacherGroupDTO]:

        query = text(
            """
            SELECT
                sg.id,
                sg.name,
                sg.subject_id,
                sg.academic_year_id
            FROM teacher_subject_assignment tsa
            JOIN subject_group sg
                ON sg.id = tsa.subject_group_id
            WHERE tsa.institutional_user_id = :teacher_id
                AND tsa.is_active = TRUE
            """
        )

        rows = self.session.execute(
            query,
            {"teacher_id": teacher_id}
        ).mappings().all()

        return [
            TeacherGroupDTO(
                id=row["id"],
                name=row["name"],
                subject_id=row["subject_id"],
                academic_year_id=row["academic_year_id"],
            )
            for row in rows
        ]
