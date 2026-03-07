from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from backend.domain.exceptions.academic_exceptions import AcademicPeriodError
from backend.domain.value_objects.academic_period_event_type import AcademicPeriodEventType


@dataclass
class AcademicPeriodEvent:
    id: UUID
    academic_period_id: UUID
    event_type: AcademicPeriodEventType
    reason: str
    performed_by_user_id: UUID
    created_at: datetime

    def __post_init__(self):
        if self.reason is None or not self.reason.strip():
            raise AcademicPeriodError("Reason is required for academic period events")
