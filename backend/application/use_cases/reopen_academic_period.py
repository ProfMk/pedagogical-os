from datetime import datetime
from uuid import uuid4

from backend.domain.entities.academic_period_event import AcademicPeriodEvent
from backend.domain.exceptions.academic_exceptions import AcademicPeriodError
from backend.domain.value_objects.academic_period_event_type import (
    AcademicPeriodEventType,
)


class ReopenAcademicPeriodUseCase:

    def __init__(
        self,
        academic_period_repository,
        event_repository,
    ):
        self.academic_period_repository = academic_period_repository
        self.event_repository = event_repository

    def execute(
        self,
        academic_period_id,
        reason,
        performed_by_user_id,
        event_id=None,
        created_at=None,
    ):

        if not reason or not reason.strip():
            raise AcademicPeriodError("Reason is required")

        period = self.academic_period_repository.get_by_id(academic_period_id)

        if not period:
            raise AcademicPeriodError("Academic period not found")

        if not period.is_closed:
            raise AcademicPeriodError("Academic period is already open")

        if event_id is None:
            event_id = uuid4()

        if created_at is None:
            created_at = datetime.utcnow()

        period.is_closed = False

        event = AcademicPeriodEvent(
            id=event_id,
            academic_period_id=academic_period_id,
            event_type=AcademicPeriodEventType.PERIOD_REOPENED,
            reason=reason,
            performed_by_user_id=performed_by_user_id,
            created_at=created_at,
        )

        self.event_repository.save(event)

        # IMPORTANTE: usar save(), no update()
        self.academic_period_repository.save(period)

        return period
