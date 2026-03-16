import pytest
import uuid
from dataclasses import dataclass


# ==========================================================
# Domain models (simplified for testing)
# ==========================================================

@dataclass
class AcademicPeriod:
    id: str
    is_closed: bool


@dataclass
class ReportCardSubjectResult:
    id: str
    academic_period_id: str
    calculated_grade: float
    final_grade: float
    override_flag: bool = False
    override_comment: str | None = None


# ==========================================================
# Domain exception
# ==========================================================

class AcademicPeriodClosedError(Exception):
    pass


# ==========================================================
# Fake repositories
# ==========================================================

class FakeAcademicPeriodRepository:

    def __init__(self):
        self.storage = {}

    def create(self, is_closed: bool):
        period = AcademicPeriod(
            id=str(uuid.uuid4()),
            is_closed=is_closed
        )
        self.storage[period.id] = period
        return period

    def get(self, period_id: str):
        return self.storage[period_id]


class FakeReportCardRepository:

    def __init__(self):
        self.storage = {}

    def create(self, academic_period_id, calculated_grade, final_grade):

        report = ReportCardSubjectResult(
            id=str(uuid.uuid4()),
            academic_period_id=academic_period_id,
            calculated_grade=calculated_grade,
            final_grade=final_grade,
        )

        self.storage[report.id] = report
        return report

    def get(self, report_card_id):
        return self.storage[report_card_id]

    def save(self, report):
        self.storage[report.id] = report


class FakeIndicatorProgressRepository:

    def __init__(self):
        self.counter = 0

    def count(self):
        return self.counter


# ==========================================================
# Use case (simplified version)
# ==========================================================

class OverrideReportCardSubjectGradeUseCase:

    def __init__(
        self,
        report_card_repository,
        academic_period_repository,
    ):
        self.report_card_repository = report_card_repository
        self.academic_period_repository = academic_period_repository

    def execute(
        self,
        report_card_id: str,
        new_grade: float,
        override_comment: str,
    ):

        report = self.report_card_repository.get(report_card_id)

        period = self.academic_period_repository.get(
            report.academic_period_id
        )

        if period.is_closed:
            raise AcademicPeriodClosedError(
                "Cannot override grade: academic period is closed."
            )

        report.final_grade = new_grade
        report.override_flag = True
        report.override_comment = override_comment

        self.report_card_repository.save(report)

        return report


# ==========================================================
# Fixtures
# ==========================================================

@pytest.fixture
def academic_period_repository():
    return FakeAcademicPeriodRepository()


@pytest.fixture
def report_card_repository():
    return FakeReportCardRepository()


@pytest.fixture
def indicator_progress_repository():
    return FakeIndicatorProgressRepository()


# ==========================================================
# Tests
# ==========================================================

def test_override_blocked_when_period_closed(
    report_card_repository,
    academic_period_repository,
):

    period = academic_period_repository.create(
        is_closed=True
    )

    report_card = report_card_repository.create(
        academic_period_id=period.id,
        calculated_grade=3.2,
        final_grade=3.2
    )

    use_case = OverrideReportCardSubjectGradeUseCase(
        report_card_repository,
        academic_period_repository,
    )

    with pytest.raises(AcademicPeriodClosedError):

        use_case.execute(
            report_card_id=report_card.id,
            new_grade=4.0,
            override_comment="Teacher correction"
        )


def test_override_allowed_when_period_open(
    report_card_repository,
    academic_period_repository,
):

    period = academic_period_repository.create(
        is_closed=False
    )

    report_card = report_card_repository.create(
        academic_period_id=period.id,
        calculated_grade=3.0,
        final_grade=3.0
    )

    use_case = OverrideReportCardSubjectGradeUseCase(
        report_card_repository,
        academic_period_repository,
    )

    result = use_case.execute(
        report_card_id=report_card.id,
        new_grade=4.5,
        override_comment="Teacher override"
    )

    assert result.final_grade == 4.5
    assert result.override_flag is True


def test_override_sets_audit_fields(
    report_card_repository,
    academic_period_repository,
):

    period = academic_period_repository.create(
        is_closed=False
    )

    report_card = report_card_repository.create(
        academic_period_id=period.id,
        calculated_grade=3.0,
        final_grade=3.0
    )

    use_case = OverrideReportCardSubjectGradeUseCase(
        report_card_repository,
        academic_period_repository,
    )

    result = use_case.execute(
        report_card_id=report_card.id,
        new_grade=4.0,
        override_comment="Manual override"
    )

    assert result.override_flag is True
    assert result.override_comment == "Manual override"


def test_override_does_not_modify_indicator_progress(
    report_card_repository,
    academic_period_repository,
    indicator_progress_repository,
):

    period = academic_period_repository.create(
        is_closed=False
    )

    progress_before = indicator_progress_repository.count()

    report_card = report_card_repository.create(
        academic_period_id=period.id,
        calculated_grade=3.0,
        final_grade=3.0
    )

    use_case = OverrideReportCardSubjectGradeUseCase(
        report_card_repository,
        academic_period_repository,
    )

    use_case.execute(
        report_card_id=report_card.id,
        new_grade=4.0,
        override_comment="Teacher correction"
    )

    progress_after = indicator_progress_repository.count()

    assert progress_before == progress_after
