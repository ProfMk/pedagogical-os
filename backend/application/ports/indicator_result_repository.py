from abc import ABC, abstractmethod
from uuid import UUID
from domain.entities.indicator_result import IndicatorResult


class IndicatorResultRepository(ABC):

    @abstractmethod
    def save(self, result: IndicatorResult) -> None:
        pass

    @abstractmethod
    def get_by_student_and_indicator(
        self,
        student_id: UUID,
        indicator_id: UUID
    ) -> IndicatorResult | None:
        pass