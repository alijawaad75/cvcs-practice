from backend.model import predict_attendance
from test_data.test_data import PATIENT_UNLIKELY_TO_ATTEND, VALID_PATIENT


def test_model_predicts_likely_attendance_for_low_risk_patient():
    prediction = predict_attendance(VALID_PATIENT)

    assert prediction["will_attend"] is True
    assert 0.5 <= prediction["confidence"] <= 0.95


def test_model_predicts_no_show_risk_for_high_risk_patient():
    prediction = predict_attendance(PATIENT_UNLIKELY_TO_ATTEND)

    assert prediction["will_attend"] is False
    assert 0.05 <= prediction["confidence"] < 0.5

