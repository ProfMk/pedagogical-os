from uuid import uuid4

from backend.application.use_cases.get_teacher_dashboard_use_case import (
    GetTeacherDashboardUseCase,
)


class MockDashboardRepository:
    def __init__(self, dataset):
        self.dataset = dataset

    def get_teacher_dashboard_dataset(self, institution_id, academic_year_id):
        return self.dataset


def test_empty_dataset_returns_empty_groups_list():
    repository = MockDashboardRepository(dataset=[])
    use_case = GetTeacherDashboardUseCase(repository=repository)

    result = use_case.execute(institution_id=uuid4(), academic_year_id=uuid4())

    assert result.groups == []
    assert result.alerts == []


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
        ]
    )
    use_case = GetTeacherDashboardUseCase(repository=repository)

    result = use_case.execute(institution_id=uuid4(), academic_year_id=uuid4())

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
        ]
    )
    use_case = GetTeacherDashboardUseCase(repository=repository)

    result = use_case.execute(institution_id=uuid4(), academic_year_id=uuid4())

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
        ]
    )
    use_case = GetTeacherDashboardUseCase(repository=repository)

    result = use_case.execute(institution_id=uuid4(), academic_year_id=uuid4())

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
        ]
    )
    use_case = GetTeacherDashboardUseCase(repository=repository)

    result = use_case.execute(institution_id=uuid4(), academic_year_id=uuid4())

    assert len(result.groups) == 1
    group = result.groups[0]
    assert group.groupId == group_id
    assert group.groupName == "Group 1"

    assert len(group.students) == 1
    student = group.students[0]
    assert student.studentId == student_id
    assert student.studentName == "Student 1"

    assert len(student.indicators) == 1
    indicator = student.indicators[0]
    assert indicator.indicatorId == indicator_id
    assert indicator.currentStage == 3
    assert indicator.totalStages == 5
    assert indicator.consolidation == 0.82
    assert indicator.normalizedLevel == 4.2

    assert result.alerts == []
