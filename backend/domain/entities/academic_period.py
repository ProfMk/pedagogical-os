# backend/domain/entities/academic_period.py

from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional
from uuid import UUID

from backend.domain.exceptions.academic_exceptions import AcademicPeriodError


@dataclass
class AcademicPeriod:
    id: UUID
    academic_year_id: UUID
    name: str
    start_date: date
    end_date: date
    is_closed: bool = False
    snapshot_generated_at: Optional[datetime] = None

    def __post_init__(self):
        if not self.name:
            raise AcademicPeriodError("Academic period name cannot be empty")

        if self.start_date > self.end_date:
            raise AcademicPeriodError("start_date must be before or equal to end_date")

    def validate_within_year(self, year_start: date, year_end: date) -> None:
        """
        Ensures the period dates fall within the academic year range.
        """
        if self.start_date < year_start:
            raise AcademicPeriodError("Period start_date is before academic year start_date")

        if self.end_date > year_end:
            raise AcademicPeriodError("Period end_date is after academic year end_date")

    def close(self, snapshot_time: datetime) -> None:
        """
        Closes the academic period and records snapshot generation time.

        Rules:
        - Cannot close twice.
        - snapshot_time must be provided.
        """
        if self.is_closed:
            raise AcademicPeriodError("Academic period is already closed")

        if snapshot_time is None:
            raise AcademicPeriodError("snapshot_time is required to close period")

        self.is_closed = True
        self.snapshot_generated_at = snapshot_time
