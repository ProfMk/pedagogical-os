from uuid import UUID
from typing import List

from backend.domain.entities.report_card_nucleus_result import ReportCardNucleusResult
from backend.domain.entities.report_card_subject_result import ReportCardSubjectResult


class ReportCardRepository:

    def save_nucleus_results(
        self,
        results: List[ReportCardNucleusResult],
    ) -> None:
        raise NotImplementedError

    def save_subject_results(
        self,
        results: List[ReportCardSubjectResult],
    ) -> None:
        raise NotImplementedError

    def delete_results_by_period(
        self,
        academic_period_id: UUID,
    ) -> None:
        raise NotImplementedError