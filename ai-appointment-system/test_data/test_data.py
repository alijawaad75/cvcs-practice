from config.rules import PHONE_EXAMPLE


VALID_PATIENT = {
    "name": "Ali Khan",
    "age": 25,
    "phone": PHONE_EXAMPLE,
    "previous_no_shows": 0,
    "reminder_opt_in": True,
}

PATIENT_UNLIKELY_TO_ATTEND = {
    "name": "Sara Ahmed",
    "age": 72,
    "phone": PHONE_EXAMPLE,
    "previous_no_shows": 3,
    "reminder_opt_in": False,
}

INVALID_PHONE_NUMBERS = [
    "03001234567",
    "+92300123456",
    "+9230012345678",
    "+913001234567",
    "not-a-phone",
]

