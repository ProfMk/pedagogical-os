from typing import List
from uuid import UUID

from sqlalchemy.orm import Session

from backend.application.ports.student_indicator_progress_reader_port import (
    StudentIndicatorProgressReaderPort
)

from backend.infrastructure.orm.student_indicator_progress_orm import (
    StudentIndicatorProgressORM
)


class StudentIndicatorProgressRepositoryORM(
    StudentIndicatorProgressReaderPort
):

    def __init__(self, session: Session):
        self.session = session

    def get_student_indicator_progress(
        self,
        student_id: UUID,
        academic_year_id: UUID
    ) -> List[dict]:

        rows = (
            self.session.query(StudentIndicatorProgressORM)
            .filter(
                StudentIndicatorProgressORM.student_id == student_id,
                StudentIndicatorProgressORM.academic_year_id == academic_year_id
            )
            .all()
        )

        results = []

        for row in rows:
            results.append(
                {
                    "indicator_id": row.indicator_id,
                    "current_stage_order": row.current_stage_order,
                    "consolidation_score": row.consolidation_score,
                    "normalized_level_internal": row.normalized_level_internal
                }
            )

        return results
