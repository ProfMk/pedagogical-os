from uuid import uuid4
from decimal import Decimal

from backend.domain.services.report_card_calculator import ReportCardCalculator


class FakeIndicatorResult:

    def __init__(self, student_id, subject_id, nucleus_id, level):
        self.student_id = student_id
        self.subject_id = subject_id
        self.nucleus_id = nucleus_id
        self.final_level = Decimal(level)


def test_report_card_calculator_generates_results():

    calculator = ReportCardCalculator()

    student_id = uuid4()
    subject_id = uuid4()
    nucleus_id = uuid4()

    indicator_results = [
        FakeIndicatorResult(student_id, subject_id, nucleus_id, 2),
        FakeIndicatorResult(student_id, subject_id, nucleus_id, 3),
    ]

    active_students = [student_id]

    nucleus_results, subject_results = calculator.calculate(
        uuid4(),
        indicator_results,
        active_students,
    )

    assert len(nucleus_results) == 1
    assert len(subject_results) == 1

    assert nucleus_results[0].final_grade == Decimal("2.50")
    assert subject_results[0].final_grade == Decimal("2.50")