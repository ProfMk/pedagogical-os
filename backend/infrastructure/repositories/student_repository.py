from typing import List
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.orm import Session

from backend.application.dtos.group_student_dto import GroupStudentDTO


class StudentRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_students_for_group(
        self,
        group_id: UUID
    ) -> List[GroupStudentDTO]:

        query = text(
            """
            SELECT
                s.id AS student_id,
                s.external_code
            FROM subject_group sg
            JOIN academic_group ag
                ON ag.id = sg.academic_group_id
            JOIN student_enrollment se
                ON se.academic_group_id = ag.id
            JOIN student s
                ON s.id = se.student_id
            WHERE sg.id = :group_id
                AND se.is_active = TRUE
            """
        )

        rows = self.session.execute(
            query,
            {"group_id": group_id}
        ).mappings().all()

        return [
            GroupStudentDTO(
                student_id=row["student_id"],
                external_code=row["external_code"],
            )
            for row in rows
        ]
