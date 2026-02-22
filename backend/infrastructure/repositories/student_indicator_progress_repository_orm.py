from typing import List
from uuid import UUID

from sqlalchemy.orm import Session, selectinload
from sqlalchemy import select

from backend.domain.entities.student_indicator_progress import (
    StudentIndicatorProgress
)
from backend.infrastructure.orm.student_indicator_progress_orm import (
    StudentIndicatorProgressORM
)
from backend.infrastructure.orm.student_orm import StudentORM


class StudentIndicatorProgressRepositoryORM:
    """
    ORM-based repository for reading StudentIndicatorProgress
    from PostgreSQL using SQLAlchemy Session.

    This repository:
    - performs ONLY data access
    - performs NO aggregation
    - performs NO business logic
    """

    def __init__(self, session: Session):
        self.session = session

    def get_by_group_and_indicator(
        self,
        group_id: str,
        indicator_id: UUID,
    ) -> List[StudentIndicatorProgress]:
        """
        Returns all StudentIndicatorProgress domain entities
        for students belonging to a given group and indicator.
        """

        stmt = (
            select(StudentIndicatorProgressORM)
            .join(StudentORM, StudentORM.id == StudentIndicatorProgressORM.student_id)
            .where(StudentORM.group_id == group_id)
            .where(StudentIndicatorProgressORM.indicator_id == indicator_id)
        )

        results = self.session.execute(stmt).scalars().all()

        return [
            StudentIndicatorProgress(
                student_id=orm_obj.student_id,
                indicator_id=orm_obj.indicator_id,
                current_stage_order=orm_obj.current_stage_order,
                consolidation_score=float(orm_obj.consolidation_score),
            )
            for orm_obj in results
        ]
