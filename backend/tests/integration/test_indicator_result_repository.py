import uuid
from decimal import Decimal
from datetime import datetime, date

from backend.infrastructure.orm.session import SessionLocal

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

from backend.infrastructure.repositories.indicator_result_repository_orm import (
    IndicatorResultRepositoryORM,
)

from backend.domain.entities.indicator_result import IndicatorResult


def test_save_and_get_indicator_result():

    session = SessionLocal()
    repository = IndicatorResultRepositoryORM(session)

    # ==========================================================
    # 1. Institution
    # ==========================================================

    institution = InstitutionORM(
        id=uuid.uuid4(),
        identity={"name": "Test School"},
        governance={"type": "private"},
        pedagogical_framework={"model": "standard"},
        organization_model="standard",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    session.add(institution)
    session.flush()

    # ==========================================================
    # 2. Academic Year
    # ==========================================================

    academic_year = AcademicYearORM(
        id=uuid.uuid4(),
        institution_id=institution.id,
        name="2026",
        start_date=date(2026, 1, 1),
        end_date=date(2026, 12, 31),
        status="active",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    session.add(academic_year)
    session.flush()

    # ==========================================================
    # 3. Academic Period
    # ==========================================================

    academic_period = AcademicPeriodORM(
        id=uuid.uuid4(),
        academic_year_id=academic_year.id,
        name="Q1",
        start_date=date(2026, 1, 1),
        end_date=date(2026, 3, 31),
        is_closed=False,
        snapshot_generated_at=None,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    session.add(academic_period)
    session.flush()

    # ==========================================================
    # 4. Academic Level
    # ==========================================================

    academic_level = AcademicLevelORM(
        id=uuid.uuid4(),
        institution_id=institution.id,
        name="Primary",
        order_index=1,
        education_stage="basic",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    session.add(academic_level)
    session.flush()

    # ==========================================================
    # 5. Academic Grade
    # ==========================================================

    academic_grade = AcademicGradeORM(
        id=uuid.uuid4(),
        institution_id=institution.id,
        academic_level_id=academic_level.id,
        name="Grade 5",
        order_index=1,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    session.add(academic_grade)
    session.flush()

    # ==========================================================
    # 6. Subject
    # ==========================================================

    subject = SubjectORM(
        id=uuid.uuid4(),
        institution_id=institution.id,
        name="Mathematics",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    session.add(subject)
    session.flush()

    # ==========================================================
    # 7. Curriculum Version
    # ==========================================================

    curriculum_version = CurriculumVersionORM(
        id=uuid.uuid4(),
        institution_id=institution.id,
        academic_year_id=academic_year.id,
        academic_level_id=academic_level.id,
        academic_grade_id=academic_grade.id,
        subject_id=subject.id,
        version_number=1,
        status="active",
        parent_version_id=None,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    session.add(curriculum_version)
    session.flush()

    # ==========================================================
    # 8. Nucleus
    # ==========================================================

    nucleus = NucleusORM(
        id=uuid.uuid4(),
        name="Numbers",
        description="Numerical reasoning",
        curriculum_version_id=curriculum_version.id,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    session.add(nucleus)
    session.flush()

    # ==========================================================
    # 9. Competency
    # ==========================================================

    competency = CompetencyORM(
        id=uuid.uuid4(),
        nucleus_id=nucleus.id,
        description="Solve problems",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    session.add(competency)
    session.flush()

    # ==========================================================
    # 10. Indicator
    # ==========================================================

    indicator = IndicatorORM(
        id=uuid.uuid4(),
        competency_id=competency.id,
        description="Test Indicator",
        total_stages=4,
        version_number=1,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    session.add(indicator)
    session.flush()

    # ==========================================================
    # 11. Student
    # ==========================================================

    student = StudentORM(
        id=uuid.uuid4(),
        institution_id=institution.id,
        external_code="S001",
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    session.add(student)
    session.commit()

    # ==========================================================
    # 12. Indicator Result (Domain -> Repository)
    # ==========================================================

    result = IndicatorResult(
        id=uuid.uuid4(),
        academic_year_id=academic_year.id,
        academic_period_id=academic_period.id,
        student_id=student.id,
        indicator_id=indicator.id,
        calculated_level=Decimal("3.50"),
        final_level=Decimal("3.50"),
        override_flag=False,
        override_comment=None,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    repository.save(result)

    # ==========================================================
    # 13. Retrieve
    # ==========================================================

    retrieved = repository.get_by_scope(
        academic_period_id=academic_period.id,
        student_id=student.id,
        indicator_id=indicator.id,
    )

    assert retrieved is not None
    assert retrieved.calculated_level == Decimal("3.50")
    assert retrieved.final_level == Decimal("3.50")
    assert retrieved.override_flag is False

    session.close()