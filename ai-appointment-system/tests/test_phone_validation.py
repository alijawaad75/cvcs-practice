import pytest

from backend.validation import validate_phone
from test_data.test_data import INVALID_PHONE_NUMBERS, VALID_PATIENT


def test_valid_phone_number_passes():
    assert validate_phone(VALID_PATIENT["phone"]) is None


@pytest.mark.parametrize("phone", INVALID_PHONE_NUMBERS)
def test_invalid_phone_numbers_fail(phone):
    assert "Phone must" in validate_phone(phone)

