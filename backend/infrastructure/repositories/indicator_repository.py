from decimal import Decimal
from typing import List
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.orm import Session

from backend.application.dtos.student_indicator_dto import StudentIndicatorDTO


class IndicatorRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_indicators_for_student(
        self,
        student_id: UUID
    ) -> List[StudentIndicatorDTO]:

        query = text(
            """
            SELECT
                i.id AS indicator_id,
                i.description AS indicator_description,
                sip.current_stage_order,
                sip.consolidation_score
            FROM student_indicator_progress sip
            JOIN indicator i
                ON i.id = sip.indicator_id
            WHERE sip.student_id = :student_id
            """
        )

        rows = self.session.execute(
            query,
            {"student_id": student_id}
        ).mappings().all()

        return [
            StudentIndicatorDTO(
                indicator_id=row["indicator_id"],
                indicator_description=row["indicator_description"],
                current_stage_order=row["current_stage_order"],
                consolidation_score=row["consolidation_score"]
                if row["consolidation_score"] is not None
                else Decimal("0"),
            )
            for row in rows
        ]
