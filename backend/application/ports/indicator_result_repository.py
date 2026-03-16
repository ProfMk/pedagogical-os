from abc import ABC, abstractmethod
from uuid import UUID
from backend.domain.entities.indicator_result import IndicatorResult


class IndicatorResultRepository(ABC):

    @abstractmethod
    def save(self, result: IndicatorResult) -> None:
        """
        Persists the indicator result (insert or update).
        """
        pass

    @abstractmethod
    def get_by_scope(
        self,
        academic_period_id: UUID,
        student_id: UUID,
        indicator_id: UUID
    ) -> IndicatorResult | None:
        """
        Retrieves an indicator result by period scope.
        """
        pass
