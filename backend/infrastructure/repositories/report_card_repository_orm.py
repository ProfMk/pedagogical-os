from uuid import UUID
from typing import List

from sqlalchemy.orm import Session

from backend.application.ports.report_card_repository import ReportCardRepository
from backend.domain.entities.report_card_nucleus_result import ReportCardNucleusResult
from backend.domain.entities.report_card_subject_result import ReportCardSubjectResult

from backend.infrastructure.orm.report_card_nucleus_result import (
    ReportCardNucleusResult as ReportCardNucleusResultORM,
)
from backend.infrastructure.orm.report_card_subject_result import (
    ReportCardSubjectResult as ReportCardSubjectResultORM,
)


class ReportCardRepositoryORM(ReportCardRepository):

    def __init__(self, session: Session):
        self._session = session

    # ==========================================================
    # DELETE RESULTS BY PERIOD
    # ==========================================================

    def delete_results_by_period(self, academic_period_id: UUID) -> None:

        self._session.query(ReportCardNucleusResultORM).filter(
            ReportCardNucleusResultORM.academic_period_id == academic_period_id
        ).delete()

        self._session.query(ReportCardSubjectResultORM).filter(
            ReportCardSubjectResultORM.academic_period_id == academic_period_id
        ).delete()

        self._session.commit()

    # ==========================================================
    # SAVE NUCLEUS RESULTS
    # ==========================================================

    def save_nucleus_results(
        self,
        results: List[ReportCardNucleusResult],
    ) -> None:

        for result in results:

            orm_obj = ReportCardNucleusResultORM(
                id=result.id,
                student_id=result.student_id,
                subject_id=result.subject_id,
                nucleus_id=result.nucleus_id,
                academic_period_id=result.academic_period_id,
                calculated_grade=result.calculated_grade,
                final_grade=result.final_grade,
                teacher_observation=result.teacher_observation,
                override_flag=result.override_flag,
                created_at=result.created_at,
                updated_at=result.updated_at,
            )

            self._session.add(orm_obj)

        self._session.commit()

    # ==========================================================
    # SAVE SUBJECT RESULTS
    # ==========================================================

    def save_subject_results(
        self,
        results: List[ReportCardSubjectResult],
    ) -> None:

        for result in results:

            orm_obj = ReportCardSubjectResultORM(
                id=result.id,
                student_id=result.student_id,
                subject_id=result.subject_id,
                academic_period_id=result.academic_period_id,
                calculated_grade=result.calculated_grade,
                final_grade=result.final_grade,
                teacher_observation=result.teacher_observation,
                override_flag=result.override_flag,
                created_at=result.created_at,
                updated_at=result.updated_at,
            )

            self._session.add(orm_obj)

        self._session.commit()