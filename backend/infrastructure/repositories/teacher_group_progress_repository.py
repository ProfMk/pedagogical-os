from typing import List
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.orm import Session

from backend.application.ports.teacher_group_progress_repository_port import (
    TeacherGroupProgressRepositoryPort,
)


class TeacherGroupProgressRepository(TeacherGroupProgressRepositoryPort):

    def __init__(self, session: Session):
        self.session = session

    def get_group_progress_tree(
        self,
        institution_id: UUID,
        academic_year_id: UUID,
        teacher_id: UUID,
        subject_id: UUID,
        group_id: UUID,
    ) -> List[dict]:
        query = text(
            """
            SELECT
                ag.id AS group_id,
                ag.name AS group_name,
                n.id AS nucleus_id,
                n.name AS nucleus_name,
                c.id AS competency_id,
                c.description AS competency_description,
                i.id AS indicator_id,
                i.description AS indicator_description,
                i.total_stages AS total_stages,
                AVG(sip.current_stage_order) AS stage_average,
                AVG(sip.consolidation_score) AS consolidation_average
            FROM student_indicator_progress sip
            JOIN student s
                ON s.id = sip.student_id
            JOIN student_enrollment se
                ON se.student_id = s.id
                AND se.academic_year_id = sip.academic_year_id
            JOIN academic_group ag
                ON ag.id = se.academic_group_id
            JOIN subject_group sg
                ON sg.academic_group_id = ag.id
            JOIN teacher_subject_assignment tsa
                ON tsa.subject_group_id = sg.id
            JOIN indicator i
                ON i.id = sip.indicator_id
            JOIN competency c
                ON c.id = i.competency_id
            JOIN nucleus n
                ON n.id = c.nucleus_id
            WHERE
                sip.academic_year_id = :academic_year_id
                AND sip.indicator_id = i.id
                AND se.academic_group_id = :group_id
                AND se.is_active = TRUE
                AND sg.subject_id = :subject_id
                AND sg.academic_group_id = :group_id
                AND tsa.institutional_user_id = :teacher_id
                AND tsa.subject_group_id = sg.id
                AND tsa.is_active = TRUE
                AND s.institution_id = :institution_id
            GROUP BY
                ag.id,
                ag.name,
                n.id,
                n.name,
                c.id,
                c.description,
                i.id,
                i.description,
                i.total_stages
            ORDER BY
                n.name,
                c.description,
                i.description
            """
        )

        result = self.session.execute(
            query,
            {
                "institution_id": institution_id,
                "academic_year_id": academic_year_id,
                "teacher_id": teacher_id,
                "subject_id": subject_id,
                "group_id": group_id,
            },
        )

        return list(result.mappings().all())
