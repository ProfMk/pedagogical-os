import time
from uuid import UUID

from backend.application.dto.teacher_dashboard_dto import (
    GroupDashboardDTO,
    IndicatorDashboardDTO,
    StudentDashboardDTO,
    TeacherDashboardResponse,
    PeriodStateDTO,
    TimelineContextDTO,
)


class GetTeacherDashboardUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(
        self,
        institution_id: UUID,
        academic_year_id: UUID,
        institutional_user_id: UUID,
    ) -> TeacherDashboardResponse:

        # -----------------------------
        # TOTAL START
        # -----------------------------
        start_total = time.time()

        # -----------------------------
        # DB FETCH (MEASURED)
        # -----------------------------
        start_db = time.time()

        dataset = self.repository.get_teacher_dashboard_dataset(
            institution_id=institution_id,
            academic_year_id=academic_year_id,
            institutional_user_id=institutional_user_id,
        )

        period_data = self.repository.get_active_academic_period(
            academic_year_id=academic_year_id
        )

        end_db = time.time()

        print("DB FETCH TIME:", (end_db - start_db) * 1000, "ms")

        # -----------------------------
        # PROCESSING START
        # -----------------------------
        start_processing = time.time()

        # -----------------------------
        # EDGE CASE
        # -----------------------------
        if not dataset:
            end_processing = time.time()
            end_total = time.time()

            print("PROCESSING TIME:", (end_processing - start_processing) * 1000, "ms")
            print("TOTAL TIME:", (end_total - start_total) * 1000, "ms")

            return TeacherDashboardResponse(
                groups=[],
                alerts=[],
                period=self._build_period_dto(period_data),
            )

        # -----------------------------
        # AGGREGATION (UNCHANGED)
        # -----------------------------
        groups_map: dict = {}

        for row in dataset:
            group_id = row["group_id"]
            student_id = row["student_id"]
            indicator_id = row["indicator_id"]
            indicator_description = row["indicator_description"]

            group_entry = groups_map.setdefault(
                group_id,
                {
                    "groupId": group_id,
                    "groupName": row["group_name"],
                    "students_map": {},
                },
            )

            students_map = group_entry["students_map"]

            student_entry = students_map.setdefault(
                student_id,
                {
                    "studentId": student_id,
                    "studentName": row["student_name"],
                    "indicators_map": {},
                },
            )

            indicators_map = student_entry["indicators_map"]

            if indicator_id is None or indicator_description is None:
                continue

            indicator_values = {
                "currentStage": row["current_stage_order"],
                "totalStages": row["total_stages"],
                "consolidation": row["consolidation_score"],
                "normalizedLevel": row["normalized_level_internal"],
            }

            existing_indicator = indicators_map.get(indicator_id)

            if existing_indicator is None:
                indicators_map[indicator_id] = IndicatorDashboardDTO(
                    indicator_id=indicator_id,
                    indicator_description=indicator_description,
                    currentStage=indicator_values["currentStage"],
                    totalStages=indicator_values["totalStages"],
                    consolidation=indicator_values["consolidation"],
                    normalizedLevel=indicator_values["normalizedLevel"],
                )
                continue

            if (
                existing_indicator.currentStage != indicator_values["currentStage"]
                or existing_indicator.totalStages != indicator_values["totalStages"]
                or existing_indicator.consolidation != indicator_values["consolidation"]
                or existing_indicator.normalizedLevel != indicator_values["normalizedLevel"]
            ):
                raise ValueError(
                    "Inconsistent duplicate indicator row detected"
                )

        # -----------------------------
        # BUILD RESPONSE
        # -----------------------------
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

        # -----------------------------
        # PROCESSING END
        # -----------------------------
        end_processing = time.time()
        end_total = time.time()

        print("PROCESSING TIME:", (end_processing - start_processing) * 1000, "ms")
        print("TOTAL TIME:", (end_total - start_total) * 1000, "ms")

        # -----------------------------
        # RESPONSE
        # -----------------------------
        return TeacherDashboardResponse(
            groups=groups,
            alerts=[],
            period=self._build_period_dto(period_data),
        )

    # ---------------------------------------
    # PERIOD DTO (NO TIMING HERE)
    # ---------------------------------------
    def _build_period_dto(self, period_data):
        if period_data is None:
            return None

        return PeriodStateDTO(
            activePeriodId=period_data["id"],
            periodName=period_data["name"],
            periodStatus="OPEN" if period_data["is_closed"] is False else "CLOSED",
            timelineContext=TimelineContextDTO(
                startDate=period_data["start_date"],
                endDate=period_data["end_date"],
            ),
        )
