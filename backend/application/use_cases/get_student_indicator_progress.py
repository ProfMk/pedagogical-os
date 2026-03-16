from uuid import UUID
from typing import List

from backend.application.ports.student_indicator_progress_reader_port import (
    StudentIndicatorProgressReaderPort
)


class GetStudentIndicatorProgressUseCase:

    def __init__(
        self,
        repository: StudentIndicatorProgressReaderPort
    ):
        self.repository = repository

    def execute(
        self,
        student_id: UUID,
        academic_year_id: UUID
    ) -> List[dict]:

        progress = self.repository.get_student_indicator_progress(
            student_id=student_id,
            academic_year_id=academic_year_id
        )

        return progress
