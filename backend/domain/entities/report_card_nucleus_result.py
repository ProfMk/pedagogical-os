from uuid import UUID
from decimal import Decimal
from datetime import datetime


class ReportCardNucleusResult:

    def __init__(
        self,
        id: UUID,
        student_id: UUID,
        subject_id: UUID,
        nucleus_id: UUID,
        academic_period_id: UUID,
        calculated_grade: Decimal | None,
        final_grade: Decimal | None,
        teacher_observation: str | None,
        override_flag: bool,
        created_at: datetime,
        updated_at: datetime,
    ):
        self.id = id
        self.student_id = student_id
        self.subject_id = subject_id
        self.nucleus_id = nucleus_id
        self.academic_period_id = academic_period_id
        self.calculated_grade = calculated_grade
        self.final_grade = final_grade
        self.teacher_observation = teacher_observation
        self.override_flag = override_flag
        self.created_at = created_at
        self.updated_at = updated_at
