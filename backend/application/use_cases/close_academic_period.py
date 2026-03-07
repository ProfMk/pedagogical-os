from datetime import datetime
from uuid import uuid4

from backend.domain.services.report_card_calculator import ReportCardCalculator
from backend.domain.exceptions.period_already_closed import PeriodAlreadyClosed
from backend.domain.entities.academic_period_event import AcademicPeriodEvent
from backend.domain.value_objects.academic_period_event_type import (
    AcademicPeriodEventType,
)


class CloseAcademicPeriodUseCase:

    def __init__(
        self,
        academic_period_repository,
        indicator_result_repository,
        student_enrollment_repository,
        report_card_repository,
        event_repository,
    ):

        self.academic_period_repository = academic_period_repository
        self.indicator_result_repository = indicator_result_repository
        self.student_enrollment_repository = student_enrollment_repository
        self.report_card_repository = report_card_repository
        self.event_repository = event_repository

        self.calculator = ReportCardCalculator()

    def execute(
        self,
        academic_period_id,
        performed_by_user_id,
        reason="Academic period closed",
        event_id=None,
        created_at=None,
    ):

        period = self.academic_period_repository.get_by_id(academic_period_id)

        if period.is_closed:
            raise PeriodAlreadyClosed()

        indicator_results = self.indicator_result_repository.get_all_by_period(
            academic_period_id
        )

        active_students = self.student_enrollment_repository.get_active_students(
            period.academic_year_id
        )

        nucleus_results, subject_results = self.calculator.calculate(
            academic_period_id,
            indicator_results,
            active_students,
        )

        self.report_card_repository.save_nucleus_results(nucleus_results)
        self.report_card_repository.save_subject_results(subject_results)

        period.is_closed = True

        if event_id is None:
            event_id = uuid4()

        if created_at is None:
            created_at = datetime.utcnow()

        event = AcademicPeriodEvent(
            id=event_id,
            academic_period_id=academic_period_id,
            event_type=AcademicPeriodEventType.PERIOD_CLOSED,
            reason=reason,
            performed_by_user_id=performed_by_user_id,
            created_at=created_at,
        )

        self.event_repository.save(event)

        self.academic_period_repository.save(period)

        return period