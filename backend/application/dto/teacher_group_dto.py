from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class TeacherGroupDTO:
    id: UUID
    name: str
    subject_id: UUID
    academic_year_id: UUID
