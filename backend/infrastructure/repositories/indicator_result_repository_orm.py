from uuid import UUID
from decimal import Decimal
from sqlalchemy.orm import Session

from backend.application.ports.indicator_result_repository import (
    IndicatorResultRepository,
)
from backend.domain.entities.indicator_result import IndicatorResult
from backend.infrastructure.orm.indicator_result_orm import IndicatorResultORM


class IndicatorResultRepositoryORM(IndicatorResultRepository):

    def __init__(self, session: Session):
        self._session = session

    # ==========================================================
    # GET BY SCOPE (PERIOD-BASED)
    # ==========================================================

    def get_by_scope(
        self,
        academic_period_id: UUID,
        student_id: UUID,
        indicator_id: UUID,
    ) -> IndicatorResult | None:

        orm_obj = (
            self._session.query(IndicatorResultORM)
            .filter_by(
                academic_period_id=academic_period_id,
                student_id=student_id,
                indicator_id=indicator_id,
            )
            .one_or_none()
        )

        if orm_obj is None:
            return None

        return self._to_domain(orm_obj)

    # ==========================================================
    # SAVE (UPSERT LOGIC)
    # ==========================================================

    def save(self, result: IndicatorResult) -> None:

        orm_obj = (
            self._session.query(IndicatorResultORM)
            .filter_by(id=result.id)
            .one_or_none()
        )

        if orm_obj is None:
            # INSERT
            orm_obj = IndicatorResultORM(
                id=result.id,
                academic_year_id=result.academic_year_id,
                academic_period_id=result.academic_period_id,
                student_id=result.student_id,
                indicator_id=result.indicator_id,
                calculated_level=result.calculated_level,
                final_level=result.final_level,
                override_flag=result.override_flag,
                override_comment=result.override_comment,
                created_at=result.created_at,
                updated_at=result.updated_at,
            )
            self._session.add(orm_obj)

        else:
            # UPDATE EXISTING
            orm_obj.academic_year_id = result.academic_year_id
            orm_obj.academic_period_id = result.academic_period_id
            orm_obj.student_id = result.student_id
            orm_obj.indicator_id = result.indicator_id
            orm_obj.calculated_level = result.calculated_level
            orm_obj.final_level = result.final_level
            orm_obj.override_flag = result.override_flag
            orm_obj.override_comment = result.override_comment
            orm_obj.updated_at = result.updated_at

        self._session.commit()

    # ==========================================================
    # EXPLICIT UPDATE (USED BY INTEGRATION TESTS)
    # ==========================================================

    def update(self, result: IndicatorResult) -> None:

        orm_obj = (
            self._session.query(IndicatorResultORM)
            .filter_by(id=result.id)
            .one()
        )

        orm_obj.final_level = result.final_level
        orm_obj.override_flag = result.override_flag
        orm_obj.override_comment = result.override_comment
        orm_obj.updated_at = result.updated_at

        self._session.commit()

    # ==========================================================
    # MAPPER
    # ==========================================================

    def _to_domain(self, orm_obj: IndicatorResultORM) -> IndicatorResult:

        return IndicatorResult(
            id=orm_obj.id,
            academic_year_id=orm_obj.academic_year_id,
            academic_period_id=orm_obj.academic_period_id,
            student_id=orm_obj.student_id,
            indicator_id=orm_obj.indicator_id,
            calculated_level=Decimal(orm_obj.calculated_level),
            final_level=Decimal(orm_obj.final_level),
            override_flag=orm_obj.override_flag,
            override_comment=orm_obj.override_comment,
            created_at=orm_obj.created_at,
            updated_at=orm_obj.updated_at,
        )