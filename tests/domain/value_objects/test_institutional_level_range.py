import pytest
from domain.value_objects.institutional_level_range import (
    InstitutionalLevelRange,
    convert_internal_to_institutional_level,
)


def test_value_inside_range():
    level = InstitutionalLevelRange(
        label="BUONO",
        lower_bound=3.0,
        upper_bound=3.9,
        order_index=3,
    )

    assert level.contains(3.5) is True


def test_value_on_lower_bound_is_valid():
    level = InstitutionalLevelRange("BUONO", 3.0, 3.9, 3)
    assert level.contains(3.0) is True


def test_value_on_upper_bound_is_valid():
    level = InstitutionalLevelRange("BUONO", 3.0, 3.9, 3)
    assert level.contains(3.9) is True


def test_value_outside_range_is_invalid():
    level = InstitutionalLevelRange("BUONO", 3.0, 3.9, 3)
    assert level.contains(2.9) is False
    assert level.contains(4.0) is False


def test_invalid_range_raises_error():
    with pytest.raises(ValueError):
        InstitutionalLevelRange("INVALID", 4.0, 3.0, 1)


def test_conversion_returns_correct_level():
    ranges = [
        InstitutionalLevelRange("SUFFICIENTE", 1.0, 2.5, 1),
        InstitutionalLevelRange("DISCRETO", 2.6, 3.2, 2),
        InstitutionalLevelRange("BUONO", 3.3, 3.8, 3),
        InstitutionalLevelRange("OTTIMO", 3.9, 5.0, 4),
    ]

    result = convert_internal_to_institutional_level(3.5, ranges)

    assert result.label == "BUONO"


def test_conversion_without_ranges_raises_error():
    with pytest.raises(ValueError):
        convert_internal_to_institutional_level(3.0, [])


def test_conversion_without_matching_range_raises_error():
    ranges = [
        InstitutionalLevelRange("LOW", 1.0, 2.0, 1),
        InstitutionalLevelRange("MID", 2.1, 3.0, 2),
    ]

    with pytest.raises(ValueError):
        convert_internal_to_institutional_level(4.5, ranges)
