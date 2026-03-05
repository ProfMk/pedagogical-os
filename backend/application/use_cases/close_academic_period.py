from backend.domain.services.report_card_calculator import ReportCardCalculator
from backend.domain.exceptions.period_already_closed import PeriodAlreadyClosed


class CloseAcademicPeriodUseCase:

    def __init__(
        self,
        academic_period_repository,
        indicator_result_repository,
        student_enrollment_repository,
        report_card_repository,
    ):

        self.academic_period_repository = academic_period_repository
        self.indicator_result_repository = indicator_result_repository
        self.student_enrollment_repository = student_enrollment_repository
        self.report_card_repository = report_card_repository

        self.calculator = ReportCardCalculator()

    def execute(self, academic_period_id):

        period = self.academic_period_repository.get_by_id(academic_period_id)

        if period.is_closed:
            raise PeriodAlreadyClosed()

        indicator_results = self.indicator_result_repository.get_all_by_period(
            academic_period_id
        )

        # 👇 ESTA ES LA LÍNEA CORRECTA
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

        self.academic_period_repository.save(period)