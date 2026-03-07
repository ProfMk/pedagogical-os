from abc import ABC, abstractmethod
from typing import List
from uuid import UUID


class IndicatorGroupProgressReaderPort(ABC):

    @abstractmethod
    def get_group_indicator_progress(
        self,
        academic_group_id: UUID,
        indicator_id: UUID
    ) -> List[dict]:
        """
        Returns indicator progress for all students in a group.
        """
        pass