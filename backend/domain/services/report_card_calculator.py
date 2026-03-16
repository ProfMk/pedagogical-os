from collections import defaultdict
from decimal import Decimal
from uuid import UUID, uuid4
from datetime import datetime

from backend.domain.entities.report_card_nucleus_result import (
    ReportCardNucleusResult,
)
from backend.domain.entities.report_card_subject_result import (
    ReportCardSubjectResult,
)


class ReportCardCalculator:

    def calculate(
        self,
        academic_period_id: UUID,
        indicator_results,
        active_students,
    ):

        nucleus_results = self._calculate_nucleus_results(
            academic_period_id,
            indicator_results,
        )

        subject_results = self._calculate_subject_results(
            academic_period_id,
            nucleus_results,
        )

        return nucleus_results, subject_results

    # ==========================================================
    # NUCLEUS RESULTS
    # ==========================================================

    def _calculate_nucleus_results(
        self,
        academic_period_id: UUID,
        indicator_results,
    ):

        grouped = defaultdict(list)

        for result in indicator_results:

            if result.final_level is None:
                continue

            if result.final_level == Decimal("0"):
                continue

            # resolve attributes safely (FakeIndicatorResult vs real entity)
            nucleus_id = getattr(result, "nucleus_id", None)
            subject_id = getattr(result, "subject_id", None)

            # if structure is missing we skip
            if nucleus_id is None or subject_id is None:
                continue

            key = (
                result.student_id,
                nucleus_id,
                subject_id,
            )

            grouped[key].append(Decimal(result.final_level))

        nucleus_results = []

        for (student_id, nucleus_id, subject_id), levels in grouped.items():

            avg = sum(levels) / Decimal(len(levels))
            avg = avg.quantize(Decimal("0.01"))

            nucleus_results.append(
                ReportCardNucleusResult(
                    id=uuid4(),
                    student_id=student_id,
                    subject_id=subject_id,
                    nucleus_id=nucleus_id,
                    academic_period_id=academic_period_id,
                    calculated_grade=avg,
                    final_grade=avg,
                    teacher_observation=None,
                    override_flag=False,
                    created_at=datetime.utcnow(),
                    updated_at=datetime.utcnow(),
                )
            )

        return nucleus_results

    # ==========================================================
    # SUBJECT RESULTS
    # ==========================================================

    def _calculate_subject_results(
        self,
        academic_period_id: UUID,
        nucleus_results,
    ):

        grouped = defaultdict(list)

        for result in nucleus_results:

            key = (
                result.student_id,
                result.subject_id,
            )

            grouped[key].append(Decimal(result.final_grade))

        subject_results = []

        for (student_id, subject_id), grades in grouped.items():

            avg = sum(grades) / Decimal(len(grades))
            avg = avg.quantize(Decimal("0.01"))

            subject_results.append(
                ReportCardSubjectResult(
                    id=uuid4(),
                    student_id=student_id,
                    subject_id=subject_id,
                    academic_period_id=academic_period_id,
                    calculated_grade=avg,
                    final_grade=avg,
                    teacher_observation=None,
                    override_flag=False,
                    created_at=datetime.utcnow(),
                    updated_at=datetime.utcnow(),
                )
            )

        return subject_results
