from backend.domain.entities.academic_period_event import AcademicPeriodEvent
from backend.domain.exceptions.academic_exceptions import AcademicPeriodError
from backend.domain.value_objects.academic_period_event_type import AcademicPeriodEventType


class ReopenAcademicPeriodUseCase:

    def __init__(self, academic_period_repository, academic_period_event_repository):
        self.academic_period_repository = academic_period_repository
        self.academic_period_event_repository = academic_period_event_repository

    def execute(
        self,
        academic_period_id,
        reason,
        performed_by_user_id,
        event_id,
        created_at,
    ):

        period = self.academic_period_repository.get_by_id(academic_period_id)

        if period is None:
            raise AcademicPeriodError("Academic period not found")

        if period.is_closed is False:
            raise AcademicPeriodError("Only closed periods can be reopened")

        if reason is None or not reason.strip():
            raise AcademicPeriodError("Reason is required to reopen academic period")

        event = AcademicPeriodEvent(
            id=event_id,
            academic_period_id=period.id,
            event_type=AcademicPeriodEventType.PERIOD_REOPENED,
            reason=reason,
            performed_by_user_id=performed_by_user_id,
            created_at=created_at,
        )

        period.is_closed = False

        self.academic_period_event_repository.save(event)
        self.academic_period_repository.save(period)

        return period
