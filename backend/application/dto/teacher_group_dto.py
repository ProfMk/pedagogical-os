from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class TeacherGroupDTO:
    id: UUID
    name: str
    subject_id: UUID
    subject_name: str
    academic_year_id: UUID
