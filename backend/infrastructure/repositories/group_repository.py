from typing import List
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.orm import Session

from backend.application.dto.teacher_group_dto import TeacherGroupDTO
from backend.application.ports.group_repository_port import GroupRepositoryPort


class GroupRepository(GroupRepositoryPort):

    def __init__(self, session: Session):
        self.session = session

    def get_groups_for_teacher(
        self,
        institution_id: UUID,
        academic_year_id: UUID,
        teacher_id: UUID,
    ) -> List[TeacherGroupDTO]:

        query = text(
            """
            SELECT DISTINCT
                ag.id AS group_id,
                ag.name AS group_name,
                sg.subject_id AS subject_id,
                s.name AS subject_name,
                ag.academic_year_id AS academic_year_id
            FROM teacher_subject_assignment tsa
            JOIN subject_group sg
                ON sg.id = tsa.subject_group_id
            JOIN subject s
                ON s.id = sg.subject_id
            JOIN academic_group ag
                ON ag.id = sg.academic_group_id
            JOIN academic_year ay
                ON ay.id = ag.academic_year_id
            WHERE tsa.institutional_user_id = :teacher_id
                AND tsa.academic_year_id = :academic_year_id
                AND tsa.is_active = TRUE
                AND sg.academic_year_id = :academic_year_id
                AND ag.academic_year_id = :academic_year_id
                AND ay.institution_id = :institution_id
            ORDER BY ag.name, sg.subject_id
            """
        )

        rows = self.session.execute(
            query,
            {
                "teacher_id": teacher_id,
                "academic_year_id": academic_year_id,
                "institution_id": institution_id,
            },
        ).mappings().all()

        return [
            TeacherGroupDTO(
                id=row["group_id"],
                name=row["group_name"],
                subject_id=row["subject_id"],
                subject_name=row["subject_name"],
                academic_year_id=row["academic_year_id"],
            )
            for row in rows
        ]