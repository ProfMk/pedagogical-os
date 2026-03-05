from uuid import UUID
from sqlalchemy.orm import Session

from backend.domain.entities.academic_period import AcademicPeriod
from backend.infrastructure.orm.academic_period_orm import AcademicPeriodORM


class AcademicPeriodRepositoryORM:

    def __init__(self, session: Session):
        self._session = session

    def get_by_id(self, academic_period_id: UUID) -> AcademicPeriod | None:

        orm_obj = (
            self._session.query(AcademicPeriodORM)
            .filter_by(id=academic_period_id)
            .one_or_none()
        )

        if orm_obj is None:
            return None

        return AcademicPeriod(
            id=orm_obj.id,
            academic_year_id=orm_obj.academic_year_id,
            name=orm_obj.name,
            start_date=orm_obj.start_date,
            end_date=orm_obj.end_date,
            is_closed=orm_obj.is_closed,
        )

    def save(self, period: AcademicPeriod) -> None:

        orm_obj = (
            self._session.query(AcademicPeriodORM)
            .filter_by(id=period.id)
            .one()
        )

        orm_obj.is_closed = period.is_closed

        self._session.commit()