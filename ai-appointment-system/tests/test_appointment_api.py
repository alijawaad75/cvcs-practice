from backend.app import handle_appointment_request
from test_data.test_data import VALID_PATIENT


class InMemoryAppointmentDatabase:
    def __init__(self):
        self.records = []

    def save(self, record):
        saved = {"id": len(self.records) + 1, **record}
        self.records.append(saved)
        return saved


def test_appointment_api_saves_valid_patient():
    db = InMemoryAppointmentDatabase()

    response = handle_appointment_request(VALID_PATIENT, db=db)

    assert response["status"] == 201
    assert response["data"]["id"] == 1
    assert response["data"]["name"] == "Ali Khan"
    assert response["data"]["prediction"]["will_attend"] is True
    assert len(db.records) == 1


def test_appointment_api_rejects_invalid_patient():
    db = InMemoryAppointmentDatabase()
    invalid_payload = {**VALID_PATIENT, "name": "A", "age": 121, "phone": "03001234567"}

    response = handle_appointment_request(invalid_payload, db=db)

    assert response["status"] == 400
    assert set(response["errors"]) == {"name", "age", "phone"}
    assert db.records == []

