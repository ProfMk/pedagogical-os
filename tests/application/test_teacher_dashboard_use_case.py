from uuid import uuid4
from datetime import date

from backend.application.use_cases.get_teacher_dashboard_use_case import (
    GetTeacherDashboardUseCase,
)


class MockDashboardRepository:
    def __init__(self, dataset, period_data=None):
        self.dataset = dataset
        self.period_data = period_data

    def get_teacher_dashboard_dataset(
        self,
        institution_id,
        academic_year_id,
        institutional_user_id,  # ✅ NUEVO PARAM
    ):
        return self.dataset

    def get_active_academic_period(self, academic_year_id):
        return self.period_data


def test_empty_dataset_returns_empty_groups_list():
    repository = MockDashboardRepository(dataset=[], period_data=None)
    use_case = GetTeacherDashboardUseCase(repository=repository)

    result = use_case.execute(
        institution_id=uuid4(),
        academic_year_id=uuid4(),
        institutional_user_id=uuid4(),  # ✅ NUEVO PARAM
    )

    assert result.groups == []
    assert result.alerts == []
    assert result.period is None


def test_multiple_groups_aggregated_correctly():
    group_1 = uuid4()
    group_2 = uuid4()
    student_1 = uuid4()
    student_2 = uuid4()
    indicator_1 = uuid4()
    indicator_2 = uuid4()

    repository = MockDashboardRepository(
        dataset=[
            {
                "group_id": group_1,
                "group_name": "A",
                "student_id": student_1,
                "student_name": "S1",
                "indicator_id": indicator_1,
                "total_stages": 5,
                "current_stage_order": 2,
                "consolidation_score": 0.6,
                "normalized_level_internal": 3.0,
            },
            {
                "group_id": group_2,
                "group_name": "B",
                "student_id": student_2,
                "student_name": "S2",
                "indicator_id": indicator_2,
                "total_stages": 5,
                "current_stage_order": 4,
                "consolidation_score": 0.9,
                "normalized_level_internal": 4.8,
            },
        ],
        period_data=None,
    )

    use_case = GetTeacherDashboardUseCase(repository=repository)

    result = use_case.execute(
        institution_id=uuid4(),
        academic_year_id=uuid4(),
        institutional_user_id=uuid4(),
    )

    assert len(result.groups) == 2
    assert {group.groupName for group in result.groups} == {"A", "B"}


def test_multiple_students_aggregated_correctly():
    group_id = uuid4()
    student_1 = uuid4()
    student_2 = uuid4()
    indicator_1 = uuid4()
    indicator_2 = uuid4()

    repository = MockDashboardRepository(
        dataset=[
            {
                "group_id": group_id,
                "group_name": "G1",
                "student_id": student_1,
                "student_name": "S1",
                "indicator_id": indicator_1,
                "total_stages": 5,
                "current_stage_order": 1,
                "consolidation_score": 0.3,
                "normalized_level_internal": 2.0,
            },
            {
                "group_id": group_id,
                "group_name": "G1",
                "student_id": student_2,
                "student_name": "S2",
                "indicator_id": indicator_2,
                "total_stages": 5,
                "current_stage_order": 3,
                "consolidation_score": 0.7,
                "normalized_level_internal": 4.0,
            },
        ],
        period_data=None,
    )

    use_case = GetTeacherDashboardUseCase(repository=repository)

    result = use_case.execute(
        institution_id=uuid4(),
        academic_year_id=uuid4(),
        institutional_user_id=uuid4(),
    )

    assert len(result.groups) == 1
    assert len(result.groups[0].students) == 2
    assert {student.studentName for student in result.groups[0].students} == {"S1", "S2"}


def test_multiple_indicators_aggregated_correctly():
    group_id = uuid4()
    student_id = uuid4()
    indicator_1 = uuid4()
    indicator_2 = uuid4()

    repository = MockDashboardRepository(
        dataset=[
            {
                "group_id": group_id,
                "group_name": "G1",
                "student_id": student_id,
                "student_name": "S1",
                "indicator_id": indicator_1,
                "total_stages": 5,
                "current_stage_order": 1,
                "consolidation_score": 0.3,
                "normalized_level_internal": 2.0,
            },
            {
                "group_id": group_id,
                "group_name": "G1",
                "student_id": student_id,
                "student_name": "S1",
                "indicator_id": indicator_2,
                "total_stages": 6,
                "current_stage_order": 4,
                "consolidation_score": 0.8,
                "normalized_level_internal": 5.0,
            },
        ],
        period_data=None,
    )

    use_case = GetTeacherDashboardUseCase(repository=repository)

    result = use_case.execute(
        institution_id=uuid4(),
        academic_year_id=uuid4(),
        institutional_user_id=uuid4(),
    )

    indicators = result.groups[0].students[0].indicators
    assert len(indicators) == 2
    assert {indicator.totalStages for indicator in indicators} == {5, 6}


def test_hierarchy_structure_is_correct():
    group_id = uuid4()
    student_id = uuid4()
    indicator_id = uuid4()

    repository = MockDashboardRepository(
        dataset=[
            {
                "group_id": group_id,
                "group_name": "Group 1",
                "student_id": student_id,
                "student_name": "Student 1",
                "indicator_id": indicator_id,
                "total_stages": 5,
                "current_stage_order": 3,
                "consolidation_score": 0.82,
                "normalized_level_internal": 4.2,
            }
        ],
        period_data=None,
    )

    use_case = GetTeacherDashboardUseCase(repository=repository)

    result = use_case.execute(
        institution_id=uuid4(),
        academic_year_id=uuid4(),
        institutional_user_id=uuid4(),
    )

    group = result.groups[0]
    student = group.students[0]
    indicator = student.indicators[0]

    assert group.groupId == group_id
    assert student.studentId == student_id
    assert indicator.indicatorId == indicator_id


def test_deterministic_ordering():
    group_low = uuid4()
    group_high = uuid4()
    if group_low > group_high:
        group_low, group_high = group_high, group_low

    class MockRepository:
        def get_teacher_dashboard_dataset(
            self, institution_id, academic_year_id, institutional_user_id
        ):
            return [
                {"group_id": group_high, "group_name": "B", "student_id": uuid4(), "student_name": "S", "indicator_id": uuid4(), "total_stages": 3, "current_stage_order": 1, "consolidation_score": 0.1, "normalized_level_internal": 0.8},
                {"group_id": group_low, "group_name": "A", "student_id": uuid4(), "student_name": "S", "indicator_id": uuid4(), "total_stages": 3, "current_stage_order": 1, "consolidation_score": 0.1, "normalized_level_internal": 0.8},
            ]

        def get_active_academic_period(self, academic_year_id):
            return None

    use_case = GetTeacherDashboardUseCase(repository=MockRepository())

    result = use_case.execute(uuid4(), uuid4(), uuid4())

    assert [g.groupId for g in result.groups] == [group_low, group_high]


# ---------------- PERIOD TESTS ----------------

def test_period_state_is_included_when_available():
    repository = MockDashboardRepository(
        dataset=[],
        period_data={
            "id": uuid4(),
            "name": "Q1",
            "start_date": date(2026, 1, 1),
            "end_date": date(2026, 3, 31),
            "is_closed": False,
        },
    )

    use_case = GetTeacherDashboardUseCase(repository=repository)

    result = use_case.execute(uuid4(), uuid4(), uuid4())

    assert result.period.periodStatus == "OPEN"


def test_period_state_closed_status():
    repository = MockDashboardRepository(
        dataset=[],
        period_data={
            "id": uuid4(),
            "name": "Q2",
            "start_date": date(2026, 4, 1),
            "end_date": date(2026, 6, 30),
            "is_closed": True,
        },
    )

    use_case = GetTeacherDashboardUseCase(repository=repository)

    result = use_case.execute(uuid4(), uuid4(), uuid4())

    assert result.period.periodStatus == "CLOSED"


def test_period_state_none_when_not_available():
    repository = MockDashboardRepository(dataset=[], period_data=None)

    use_case = GetTeacherDashboardUseCase(repository=repository)

    result = use_case.execute(uuid4(), uuid4(), uuid4())

    assert result.period is None