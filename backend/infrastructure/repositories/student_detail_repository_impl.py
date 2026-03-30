from typing import List
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.orm import Session

from backend.domain.repositories.student_detail_repository import StudentDetailRepository


class StudentDetailRepositoryImpl(StudentDetailRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_student_detail(
        self,
        institution_id: UUID,
        academic_year_id: UUID,
        student_id: UUID,
    ) -> List[dict]:
        query = text(
            """
            SELECT
                s.id AS student_id,
                s.external_code AS student_name,

                n.id AS nucleus_id,
                n.name AS nucleus_name,

                c.id AS competency_id,
                c.description AS competency_description,

                i.id AS indicator_id,
                i.description AS indicator_description,

                sip.current_stage_order AS current_stage,
                i.total_stages AS total_stages,
                sip.consolidation_score AS consolidation,

                ist.stage_order AS stage_number,
                AVG(se.raw_score)::float AS stage_consolidation,
                COUNT(se.id)::int AS evidence_count
            FROM student s
            JOIN student_indicator_progress sip
                ON sip.student_id = s.id
                AND sip.academic_year_id = :academic_year_id
            JOIN indicator i
                ON i.id = sip.indicator_id
            JOIN competency c
                ON c.id = i.competency_id
            JOIN nucleus n
                ON n.id = c.nucleus_id
            LEFT JOIN indicator_stage ist
                ON ist.indicator_id = i.id
            LEFT JOIN student_evidence se
                ON se.student_id = s.id
                AND se.academic_year_id = sip.academic_year_id
                AND se.indicator_id = i.id
                AND se.indicator_stage_id = ist.id
            WHERE
                s.id = :student_id
                AND s.institution_id = :institution_id
            GROUP BY
                s.id,
                s.external_code,
                n.id,
                n.name,
                c.id,
                c.description,
                i.id,
                i.description,
                sip.current_stage_order,
                i.total_stages,
                sip.consolidation_score,
                ist.stage_order
            ORDER BY
                n.id,
                c.id,
                i.id,
                ist.stage_order
            """
        )

        result = self.session.execute(
            query,
            {
                "institution_id": institution_id,
                "academic_year_id": academic_year_id,
                "student_id": student_id,
            },
        )

        return result.mappings().all()
