def predict_attendance(patient):
    """Small deterministic ML-like predictor for testable demo behavior."""
    age = patient["age"]
    previous_no_shows = patient.get("previous_no_shows", 0)
    reminder_opt_in = patient.get("reminder_opt_in", True)

    score = 0.65
    if reminder_opt_in:
        score += 0.15
    if previous_no_shows:
        score -= min(previous_no_shows * 0.2, 0.5)
    if age < 18 or age > 65:
        score -= 0.05

    will_attend = score >= 0.5
    return {
        "will_attend": will_attend,
        "confidence": round(max(0.05, min(score, 0.95)), 2),
    }

