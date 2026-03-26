from uuid import UUID

from backend.application.dto.teacher_dashboard_dto import (
    GroupDashboardDTO,
    IndicatorDashboardDTO,
    StudentDashboardDTO,
    TeacherDashboardResponse,
)


class GetTeacherDashboardUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(
        self,
        institution_id: UUID,
        academic_year_id: UUID,
    ) -> TeacherDashboardResponse:

        dataset = self.repository.get_teacher_dashboard_dataset(
            institution_id=institution_id,
            academic_year_id=academic_year_id,
        )

        # Edge case: empty dataset
        if not dataset:
            return TeacherDashboardResponse(groups=[], alerts=[])

        groups_map: dict = {}

        for row in dataset:
            group_id = row["group_id"]
            student_id = row["student_id"]
            indicator_id = row["indicator_id"]

            # --- GROUP ---
            group_entry = groups_map.setdefault(
                group_id,
                {
                    "groupId": group_id,
                    "groupName": row["group_name"],
                    "students_map": {},
                },
            )

            # --- STUDENT ---
            students_map = group_entry["students_map"]

            student_entry = students_map.setdefault(
                student_id,
                {
                    "studentId": student_id,
                    "studentName": row["student_name"],
                    "indicators_map": {},
                },
            )

            # --- INDICATOR ---
            indicators_map = student_entry["indicators_map"]

            indicator_values = {
                "currentStage": row["current_stage_order"],
                "totalStages": row["total_stages"],
                "consolidation": row["consolidation_score"],
                "normalizedLevel": row["normalized_level_internal"],
            }

            existing_indicator = indicators_map.get(indicator_id)

            if existing_indicator is None:
                indicators_map[indicator_id] = IndicatorDashboardDTO(
                    indicatorId=indicator_id,
                    currentStage=indicator_values["currentStage"],
                    totalStages=indicator_values["totalStages"],
                    consolidation=indicator_values["consolidation"],
                    normalizedLevel=indicator_values["normalizedLevel"],
                )
                continue

            # --- DUPLICATE VALIDATION ---
            if (
                existing_indicator.currentStage != indicator_values["currentStage"]
                or existing_indicator.totalStages != indicator_values["totalStages"]
                or existing_indicator.consolidation != indicator_values["consolidation"]
                or existing_indicator.normalizedLevel != indicator_values["normalizedLevel"]
            ):
                raise ValueError(
                    "Inconsistent duplicate indicator row detected"
                )

        # --- BUILD RESPONSE (DETERMINISTIC ORDER) ---

        groups = []

        for group_id in sorted(groups_map):
            group_entry = groups_map[group_id]
            students_map = group_entry["students_map"]

            students = []

            for student_id in sorted(students_map):
                student_entry = students_map[student_id]
                indicators_map = student_entry["indicators_map"]

                indicators = [
                    indicators_map[indicator_id]
                    for indicator_id in sorted(indicators_map)
                ]

                students.append(
                    StudentDashboardDTO(
                        studentId=student_entry["studentId"],
                        studentName=student_entry["studentName"],
                        indicators=indicators,
                    )
                )

            groups.append(
                GroupDashboardDTO(
                    groupId=group_entry["groupId"],
                    groupName=group_entry["groupName"],
                    students=students,
                )
            )

        return TeacherDashboardResponse(
            groups=groups,
            alerts=[],
        )