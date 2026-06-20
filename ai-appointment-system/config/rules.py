"""Central validation rules for the appointment system.

Changing these constants is the intended way to evolve business rules.
Tests import representative data from test_data instead of duplicating
regex details across many test files.
"""

MIN_NAME_LENGTH = 2
MIN_AGE = 1
MAX_AGE = 120

# Current maintained rule:
# Pakistani mobile numbers in international format, e.g. +923001234567.
PHONE_PATTERN = r"^\+923[0-9]{9}$"
PHONE_EXAMPLE = "+923001234567"
PHONE_RULE_DESCRIPTION = "Phone must be a Pakistani mobile number like +923001234567"

