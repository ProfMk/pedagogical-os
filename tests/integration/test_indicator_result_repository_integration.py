import pytest
from uuid import uuid4
from decimal import Decimal
from datetime import datetime, date

from sqlalchemy.orm import Session

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
from backend.infrastructure.orm.indicator_result_orm import IndicatorResultORM


@pytest.mark.integration
def test_update_override_persists_in_database(test_db_session: Session):

    # ---------------------------
    # 1. Institution
    # ---------------------------

    institution = InstitutionORM(
        id=uuid4(),
        identity={"name": "Test School"},
        governance={"type": "private"},
        pedagogical_framework={"model": "standard"},
        organization_model="standard",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    test_db_session.add(institution)

    # ---------------------------
    # 2. Academic Level
    # ---------------------------

    level = AcademicLevelORM(
        id=uuid4(),
        institution_id=institution.id,
        name="Primary",
        order_index=1,
        education_stage="basic",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    test_db_session.add(level)

    # ---------------------------
    # 3. Academic Grade
    # ---------------------------

    grade = AcademicGradeORM(
        id=uuid4(),
        institution_id=institution.id,
        academic_level_id=level.id,
        name="Grade 5",
        order_index=1,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    test_db_session.add(grade)

    # ---------------------------
    # 4. Subject
    # ---------------------------

    subject = SubjectORM(
        id=uuid4(),
        institution_id=institution.id,
        name="Mathematics",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    test_db_session.add(subject)

    # ---------------------------
    # 5. Academic Year
    # ---------------------------

    academic_year = AcademicYearORM(
        id=uuid4(),
        institution_id=institution.id,
        name="2026",
        start_date=date(2026, 1, 1),
        end_date=date(2026, 12, 31),
        status="active",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    test_db_session.add(academic_year)

    # ---------------------------
    # 6. Academic Period  (OBBLIGATORIO)
    # ---------------------------

    academic_period = AcademicPeriodORM(
        id=uuid4(),
        academic_year_id=academic_year.id,
        name="Q1",
        start_date=date(2026, 1, 1),
        end_date=date(2026, 3, 31),
        is_closed=False,
        snapshot_generated_at=None,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    test_db_session.add(academic_period)

    # ---------------------------
    # 7. Curriculum Version
    # ---------------------------

    curriculum_version = CurriculumVersionORM(
        id=uuid4(),
        institution_id=institution.id,
        academic_year_id=academic_year.id,
        academic_level_id=level.id,
        academic_grade_id=grade.id,
        subject_id=subject.id,
        version_number=1,
        status="active",
        parent_version_id=None,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    test_db_session.add(curriculum_version)

    # ---------------------------
    # 8. Nucleus
    # ---------------------------

    nucleus = NucleusORM(
        id=uuid4(),
        name="Numbers",
        description="Numerical reasoning",
        curriculum_version_id=curriculum_version.id,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    test_db_session.add(nucleus)

    # ---------------------------
    # 9. Competency
    # ---------------------------

    competency = CompetencyORM(
        id=uuid4(),
        nucleus_id=nucleus.id,
        description="Solve problems",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    test_db_session.add(competency)

    # ---------------------------
    # 10. Indicator
    # ---------------------------

    indicator = IndicatorORM(
        id=uuid4(),
        competency_id=competency.id,
        description="Problem solving level",
        total_stages=4,
        version_number=1,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    test_db_session.add(indicator)

    # ---------------------------
    # 11. Student
    # ---------------------------

    student = StudentORM(
        id=uuid4(),
        institution_id=institution.id,
        external_code="S001",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    test_db_session.add(student)

    test_db_session.commit()

    # ---------------------------
    # 12. Indicator Result (CON PERIOD)
    # ---------------------------

    result = IndicatorResultORM(
        id=uuid4(),
        academic_year_id=academic_year.id,
        academic_period_id=academic_period.id,
        student_id=student.id,
        indicator_id=indicator.id,
        calculated_level=Decimal("3.20"),
        final_level=Decimal("3.20"),
        override_flag=False,
        override_comment=None,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    test_db_session.add(result)
    test_db_session.commit()

    # ---------------------------
    # ACT – Override
    # ---------------------------

    result.override_flag = True
    result.override_comment = "Teacher override"
    result.final_level = Decimal("4.00")
    result.updated_at = datetime.utcnow()

    test_db_session.commit()

    # ---------------------------
    # ASSERT
    # ---------------------------

    persisted = (
        test_db_session
        .query(IndicatorResultORM)
        .filter_by(id=result.id)
        .first()
    )

    assert persisted is not None
    assert persisted.override_flag is True
    assert persisted.override_comment == "Teacher override"
    assert persisted.final_level == Decimal("4.00")
