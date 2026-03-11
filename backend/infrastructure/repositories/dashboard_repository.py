from typing import List
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.orm import Session


class DashboardRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_teacher_dashboard_dataset(
        self,
        institution_id: UUID,
        academic_year_id: UUID,
    ) -> List[dict]:
        query = text(
            """
            SELECT
                ag.id AS group_id,
                ag.name AS group_name,
                s.id AS student_id,
                s.external_code AS student_name,
                i.id AS indicator_id,
                i.total_stages AS total_stages,
                sip.current_stage_order AS current_stage_order,
                sip.consolidation_score AS consolidation_score,
                sip.normalized_level_internal AS normalized_level_internal
            FROM academic_group ag
            JOIN student_enrollment se
                ON se.academic_group_id = ag.id
            JOIN student s
                ON s.id = se.student_id
            JOIN student_indicator_progress sip
                ON sip.student_id = s.id
                AND sip.academic_year_id = ag.academic_year_id
            JOIN indicator i
                ON i.id = sip.indicator_id
            WHERE ag.academic_year_id = :academic_year_id
                AND s.institution_id = :institution_id
                AND se.academic_year_id = :academic_year_id
            ORDER BY
                ag.id,
                s.id,
                i.id
            """
        )

        rows = self.session.execute(
            query,
            {
                "institution_id": institution_id,
                "academic_year_id": academic_year_id,
            },
        ).mappings().all()

        return [dict(row) for row in rows]
