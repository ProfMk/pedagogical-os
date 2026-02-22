# backend/domain/entities/academic_year.py

from dataclasses import dataclass
from datetime import date
from enum import Enum
from uuid import UUID

from backend.domain.exceptions.academic_exceptions import AcademicYearError


class AcademicYearStatus(str, Enum):
    DRAFT = "draft"
    ACTIVE = "active"
    CLOSED = "closed"


@dataclass
class AcademicYear:
    id: UUID
    institution_id: UUID
    name: str
    start_date: date
    end_date: date
    status: AcademicYearStatus

    def __post_init__(self):
        if not self.name:
            raise AcademicYearError("Academic year name cannot be empty")

        if self.start_date >= self.end_date:
            raise AcademicYearError("start_date must be before end_date")

    def activate(self, existing_active_year_exists: bool) -> None:
        """
        Transitions AcademicYear from DRAFT to ACTIVE.

        Rules:
        - Only DRAFT can be activated.
        - Only one ACTIVE year per institution.
        """
        if self.status != AcademicYearStatus.DRAFT:
            raise AcademicYearError("Only draft academic year can be activated")

        if existing_active_year_exists:
            raise AcademicYearError("Another academic year is already active")

        self.status = AcademicYearStatus.ACTIVE

    def close(self, open_periods_exist: bool) -> None:
        """
        Transitions AcademicYear from ACTIVE to CLOSED.

        Rules:
        - Only ACTIVE can be closed.
        - Cannot close if there are open periods.
        """
        if self.status != AcademicYearStatus.ACTIVE:
            raise AcademicYearError("Only active academic year can be closed")

        if open_periods_exist:
            raise AcademicYearError("Cannot close academic year with open periods")

        self.status = AcademicYearStatus.CLOSED