import re

from config.rules import (
    MAX_AGE,
    MIN_AGE,
    MIN_NAME_LENGTH,
    PHONE_PATTERN,
    PHONE_RULE_DESCRIPTION,
)


def validate_name(name):
    if not isinstance(name, str) or len(name.strip()) < MIN_NAME_LENGTH:
        return "Name must contain at least 2 characters"
    return None


def validate_age(age):
    if not isinstance(age, int):
        return "Age must be a whole number"
    if age < MIN_AGE or age > MAX_AGE:
        return f"Age must be between {MIN_AGE} and {MAX_AGE}"
    return None


def validate_phone(phone):
    if not isinstance(phone, str) or not re.fullmatch(PHONE_PATTERN, phone.strip()):
        return PHONE_RULE_DESCRIPTION
    return None


def validate_appointment_payload(payload):
    errors = {}
    name_error = validate_name(payload.get("name"))
    age_error = validate_age(payload.get("age"))
    phone_error = validate_phone(payload.get("phone"))

    if name_error:
        errors["name"] = name_error
    if age_error:
        errors["age"] = age_error
    if phone_error:
        errors["phone"] = phone_error

    return errors

