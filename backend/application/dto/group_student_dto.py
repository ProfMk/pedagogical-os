from dataclasses import dataclass
from typing import Optional
from uuid import UUID


@dataclass(frozen=True)
class GroupStudentDTO:
    student_id: UUID
    external_code: Optional[str]
