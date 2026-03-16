import uuid
from datetime import datetime, date

import pytest

from backend.infrastructure.orm.institution_orm import InstitutionORM
from backend.infrastructure.orm.academic_year_orm import AcademicYearORM
from backend.infrastructure.orm.academic_period_orm import AcademicPeriodORM
from backend.infrastructure.orm.academic_level_orm import AcademicLevelORM
from backend.infrastructure.orm.academic_grade_orm import AcademicGradeORM
from backend.infrastructure.orm.subject_orm import SubjectORM
from backend.infrastructure.orm.curriculum_version_orm import CurriculumVersionORM
from backend.infrastructure.orm.nucleus_orm import NucleusORM
from backend.infrastructure.orm.competency_orm import CompetencyORM
from backend.infrastructure.orm.indicator_orm import IndicatorORM
from backend.infrastructure.orm.student_orm import StudentORM
from backend.infrastructure.orm.student_enrollment_orm import StudentEnrollmentORM
from backend.infrastructure.orm.indicator_result_orm import IndicatorResultORM
from backend.infrastructure.orm.academic_group_orm import AcademicGroupORM


@pytest.fixture
def academic_context(test_db_session):

    session = test_db_session
    now = datetime.utcnow()

    # ---------------------------
    # Institution
    # ---------------------------
    institution = InstitutionORM(
        id=uuid.uuid4(),
        identity={"name": "Test School"},
        governance={"type": "private"},
        pedagogical_framework={"model": "standard"},
        organization_model="standard",
        created_at=now,
        updated_at=now,
    )
    session.add(institution)
    session.flush()

    # ---------------------------
    # Academic Level
    # ---------------------------
    level = AcademicLevelORM(
        id=uuid.uuid4(),
        institution_id=institution.id,
        name="Primary",
        order_index=1,
        education_stage="basic",
        created_at=now,
        updated_at=now,
    )
    session.add(level)
    session.flush()

    # ---------------------------
    # Academic Grade
    # ---------------------------
    grade = AcademicGradeORM(
        id=uuid.uuid4(),
        institution_id=institution.id,
        academic_level_id=level.id,
        name="Grade 5",
        order_index=1,
        created_at=now,
        updated_at=now,
    )
    session.add(grade)
    session.flush()

    # ---------------------------
    # Subject
    # ---------------------------
    subject = SubjectORM(
        id=uuid.uuid4(),
        institution_id=institution.id,
        name="Mathematics",
        created_at=now,
        updated_at=now,
    )
    session.add(subject)
    session.flush()

    # ---------------------------
    # Academic Year
    # ---------------------------
    academic_year = AcademicYearORM(
        id=uuid.uuid4(),
        institution_id=institution.id,
        name="2026",
        start_date=date(2026, 1, 1),
        end_date=date(2026, 12, 31),
        status="active",
        created_at=now,
        updated_at=now,
    )
    session.add(academic_year)
    session.flush()

    # ---------------------------
    # Academic Period
    # ---------------------------
    academic_period = AcademicPeriodORM(
        id=uuid.uuid4(),
        academic_year_id=academic_year.id,
        name="Q1",
        start_date=date(2026, 1, 1),
        end_date=date(2026, 3, 31),
        is_closed=False,
        snapshot_generated_at=None,
        created_at=now,
        updated_at=now,
    )
    session.add(academic_period)
    session.flush()

    # ---------------------------
    # Curriculum Version
    # ---------------------------
    curriculum_version = CurriculumVersionORM(
        id=uuid.uuid4(),
        institution_id=institution.id,
        academic_year_id=academic_year.id,
        academic_level_id=level.id,
        academic_grade_id=grade.id,
        subject_id=subject.id,
        version_number=1,
        status="draft",
        parent_version_id=None,
        created_at=now,
        updated_at=now,
    )
    session.add(curriculum_version)
    session.flush()

    # ---------------------------
    # Nucleus
    # ---------------------------
    nucleus = NucleusORM(
        id=uuid.uuid4(),
        name="Numbers",
        description="Numerical thinking",
        curriculum_version_id=curriculum_version.id,
        created_at=now,
        updated_at=now,
    )
    session.add(nucleus)
    session.flush()

    # ---------------------------
    # Competency
    # ---------------------------
    competency = CompetencyORM(
        id=uuid.uuid4(),
        nucleus_id=nucleus.id,
        description="Understands fractions",
        created_at=now,
        updated_at=now,
    )
    session.add(competency)
    session.flush()

    # ---------------------------
    # Indicator
    # ---------------------------
    indicator = IndicatorORM(
        id=uuid.uuid4(),
        competency_id=competency.id,
        description="Adds fractions",
        total_stages=4,
        version_number=1,
        created_at=now,
        updated_at=now,
    )
    session.add(indicator)
    session.flush()

    # ---------------------------
    # Student
    # ---------------------------
    student = StudentORM(
        id=uuid.uuid4(),
        institution_id=institution.id,
        external_code="S001",
        created_at=now,
        updated_at=now,
    )
    session.add(student)
    session.flush()

    # ---------------------------
    # Academic Group
    # ---------------------------
    academic_group = AcademicGroupORM(
        id=uuid.uuid4(),
        academic_year_id=academic_year.id,
        academic_grade_id=grade.id,
        name="5A",
        created_at=now,
        updated_at=now,
    )
    session.add(academic_group)
    session.flush()

    # ---------------------------
    # Academic Group
    # ---------------------------
    academic_group = AcademicGroupORM(
        id=uuid.uuid4(),
        academic_year_id=academic_year.id,
        academic_grade_id=grade.id,
        name="5A",
        created_at=now,
        updated_at=now,
    )

    session.add(academic_group)
    session.flush()
    # ---------------------------
    # Student Enrollment
    # ---------------------------
    enrollment = StudentEnrollmentORM(
        id=uuid.uuid4(),
        academic_year_id=academic_year.id,
        student_id=student.id,
        academic_group_id=academic_group.id,
        enrolled_at=now,
        withdrawn_at=None,
        is_active=True,
        created_at=now,
        updated_at=now,
    )

    session.add(enrollment)
    session.flush()

    # ---------------------------
    # Indicator Result
    # ---------------------------
    indicator_result = IndicatorResultORM(
        id=uuid.uuid4(),
        academic_year_id=academic_year.id,
        academic_period_id=academic_period.id,
        student_id=student.id,
        indicator_id=indicator.id,
        calculated_level=2,
        final_level=2,
        override_flag=False,
        override_comment=None,
        created_at=now,
        updated_at=now,
    )
    session.add(indicator_result)

    session.commit()

    return {
        "institution": institution,
        "academic_year": academic_year,
        "academic_period": academic_period,
        "student": student,
        "indicator": indicator,
        "student_enrollment": enrollment,
        "indicator_result": indicator_result,
    }


__all__ = ["academic_context"]
