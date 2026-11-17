
import pytest
from src.cart_delivery import qualifies_free_delivery


@pytest.mark.parametrize(
    ("total_cents", "expected"),
    [
        (0, False),     # TC-001: zero order total
        (4999, False),  # TC-002: below threshold
        (5000, True),   # TC-003: at threshold
        (5001, True),   # TC-004: above threshold
    ],
)
def test_qualifies_free_delivery_valid(total_cents, expected):
    result = qualifies_free_delivery(total_cents)

    assert result is expected


def test_qualifies_free_delivery_negative():
    with pytest.raises(ValueError):
        qualifies_free_delivery(-1)


@pytest.mark.parametrize(
    "total_cents",
    [
        5000.5,  # TC-006: float
        "5000",  # TC-007: string
        True,    # TC-008: Boolean True
        False,   # TC-009: Boolean False
    ],
)
def test_qualifies_free_delivery_invalid_type(total_cents):
    with pytest.raises(TypeError):
        qualifies_free_delivery(total_cents)
