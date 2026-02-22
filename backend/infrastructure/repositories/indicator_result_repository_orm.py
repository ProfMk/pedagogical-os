from uuid import UUID
from sqlalchemy.orm import Session
from decimal import Decimal

from application.ports.indicator_result_repository import IndicatorResultRepository
from domain.entities.indicator_result import IndicatorResult
from backend.infrastructure.orm.indicator_result_orm import IndicatorResultORM


class IndicatorResultRepositoryORM(IndicatorResultRepository):

    def __init__(self, session: Session):
        self._session = session

    def save(self, result: IndicatorResult) -> None:
        orm_obj = IndicatorResultORM(
            id=result.id,
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
        self._session.commit()

    def get_by_student_and_indicator(
        self,
        student_id: UUID,
        indicator_id: UUID
    ) -> IndicatorResult | None:

        orm_obj = (
            self._session.query(IndicatorResultORM)
            .filter_by(student_id=student_id, indicator_id=indicator_id)
            .first()
        )

        if orm_obj is None:
            return None

        return IndicatorResult(
            id=orm_obj.id,
            student_id=orm_obj.student_id,
            indicator_id=orm_obj.indicator_id,
            calculated_level=Decimal(orm_obj.calculated_level),
            final_level=Decimal(orm_obj.final_level),
            override_flag=orm_obj.override_flag,
            override_comment=orm_obj.override_comment,
            created_at=orm_obj.created_at,
            updated_at=orm_obj.updated_at,
        )