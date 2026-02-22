import uuid
from decimal import Decimal
from datetime import datetime

# 🔥 Registrar modelos ORM en metadata
import backend.infrastructure.orm.indicator_orm
import backend.infrastructure.orm.student_orm

from backend.infrastructure.orm.session import SessionLocal
from backend.infrastructure.orm.indicator_result_orm import IndicatorResultORM
from backend.infrastructure.repositories.indicator_result_repository_orm import (
    IndicatorResultRepositoryORM,
)
from backend.domain.entities.indicator_result import IndicatorResult


def test_save_and_get_indicator_result():

    session = SessionLocal()
    repository = IndicatorResultRepositoryORM(session)

    existing_student_id = uuid.UUID("f8888a93-67e7-4d2e-9729-4369a8edd371")
    existing_indicator_id = uuid.UUID("698ad1c0-3b39-4e33-81b9-2113f497b751")

    result = IndicatorResult(
        id=uuid.uuid4(),
        student_id=existing_student_id,
        indicator_id=existing_indicator_id,
        calculated_level=Decimal("3.50"),
        final_level=Decimal("3.50"),
        override_flag=False,
        override_comment=None,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )

    repository.save(result)

    retrieved = repository.get_by_student_and_indicator(
        existing_student_id,
        existing_indicator_id,
    )

    assert retrieved is not None
    assert retrieved.calculated_level == Decimal("3.50")
    assert retrieved.final_level == Decimal("3.50")
    assert retrieved.override_flag is False

    # 🔥 Limpieza controlada
    session.query(IndicatorResultORM).filter_by(
        student_id=existing_student_id,
        indicator_id=existing_indicator_id,
    ).delete()

    session.commit()
    session.close()