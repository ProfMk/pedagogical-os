from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class InstitutionalLevelRange:
    """
    Value Object.
    Represents an institutional evaluation level defined
    by a closed numeric range.
    """
    label: str
    lower_bound: float
    upper_bound: float
    order_index: int

    def __post_init__(self):
        if self.lower_bound >= self.upper_bound:
            raise ValueError(
                "lower_bound must be strictly less than upper_bound"
            )

    def contains(self, value: float) -> bool:
        return self.lower_bound <= value <= self.upper_bound


def convert_internal_to_institutional_level(
    normalized_level_internal: float,
    level_ranges: List[InstitutionalLevelRange],
) -> InstitutionalLevelRange:
    """
    Pure domain function.
    Converts an internal normalized level (1–5)
    into an institutional level using configured ranges.
    """
    if not level_ranges:
        raise ValueError("No institutional level ranges configured")

    for level_range in level_ranges:
        if level_range.contains(normalized_level_internal):
            return level_range

    raise ValueError(
        f"No institutional level range found for value {normalized_level_internal}"
    )
