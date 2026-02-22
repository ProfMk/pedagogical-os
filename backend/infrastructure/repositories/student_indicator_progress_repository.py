from uuid import UUID
from sqlalchemy.orm import Session

from backend.infrastructure.orm.student_indicator_progress_orm import (
    StudentIndicatorProgressORM
)
from backend.infrastructure.orm.student_orm import StudentORM
from backend.infrastructure.orm.indicator_orm import IndicatorORM
from backend.infrastructure.repositories.student_indicator_progress_projection import (
    StudentIndicatorProgressProjection
)


class StudentIndicatorProgressRepository:
    """
    Read-only repository for student indicator progress.
    """

    def __init__(self, session: Session):
        self.session = session

    def get_by_student_and_indicator(
        self,
        student_id: UUID,
        indicator_id: UUID
    ) -> StudentIndicatorProgressProjection:
        """
        Returns the progress of a student for a given indicator.

        Raises:
            ValueError if no record is found.
        """

        result = (
            self.session.query(
                StudentIndicatorProgressORM.student_id,
                StudentORM.name.label("student_name"),

                StudentIndicatorProgressORM.indicator_id,
                IndicatorORM.description.label("indicator_description"),

                StudentIndicatorProgressORM.current_stage,
                IndicatorORM.total_stages,

                StudentIndicatorProgressORM.normalized_level_internal,
                StudentIndicatorProgressORM.consolidation_score,
            )
            .join(
                StudentORM,
                StudentORM.id == StudentIndicatorProgressORM.student_id
            )
            .join(
                IndicatorORM,
                IndicatorORM.id == StudentIndicatorProgressORM.indicator_id
            )
            .filter(
                StudentIndicatorProgressORM.student_id == student_id,
                StudentIndicatorProgressORM.indicator_id == indicator_id
            )
            .one_or_none()
        )

        if result is None:
            raise ValueError(
                "Student indicator progress not found."
            )

        return StudentIndicatorProgressProjection(
            student_id=result.student_id,
            student_name=result.student_name,

            indicator_id=result.indicator_id,
            indicator_description=result.indicator_description,

            current_stage=result.current_stage,
            total_stages=result.total_stages,

            normalized_level_internal=result.normalized_level_internal,
            consolidation_score=result.consolidation_score
        )
