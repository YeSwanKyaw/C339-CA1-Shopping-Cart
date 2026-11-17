
import pytest
from src.cart_total import calculate_total


@pytest.mark.parametrize(
    ("unit_price", "quantity", "expected_total"),
    [
        (1250, 3, 3750),  # TC-001: positive price and quantity
        (0, 3, 0),        # TC-002: zero unit price
        (1250, 0, 0),     # TC-003: zero quantity
        (1, 3, 3),        # TC-004: minimum positive price
        (1250, 1, 1250),  # TC-005: minimum positive quantity
    ],
)
def test_calculate_total_valid(unit_price, quantity, expected_total):
    result = calculate_total(unit_price, quantity)

    assert result == expected_total
    assert type(result) is int


@pytest.mark.parametrize(
    ("unit_price", "quantity"),
    [
        (-1, 3),     # TC-006: negative unit price
        (1250, -1),  # TC-007: negative quantity
    ],
)
def test_calculate_total_negative(unit_price, quantity):
    with pytest.raises(ValueError):
        calculate_total(unit_price, quantity)


@pytest.mark.parametrize(
    ("unit_price", "quantity"),
    [
        (1.5, 3),      # TC-008: float unit price
        ("1", 3),      # TC-009: string unit price
        (True, 3),     # TC-010: True unit price
        (False, 3),    # TC-011: False unit price
        (1250, 1.5),   # TC-012: float quantity
        (1250, "1"),   # TC-013: string quantity
        (1250, True),  # TC-014: True quantity
        (1250, False), # TC-015: False quantity
    ],
)
def test_calculate_total_invalid_type(unit_price, quantity):
    with pytest.raises(TypeError):
        calculate_total(unit_price, quantity)
