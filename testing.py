# tests/test_digit_app.py

import pandas as pd
from digit_app import (
    upload_image,
    preprocess_image,
    predict_digit,
    save_prediction_history
)

def test_tc_01_image_upload():
    result = upload_image("digit7.png")
    assert result == True


def test_tc_02_image_preprocessing():
    result = preprocess_image("digit7.png")

    assert result["size"] == (28, 28)
    assert result["mode"] == "grayscale"
    assert result["normalized"] == True


def test_tc_03_digit_prediction():
    result = predict_digit("digit7.png")

    assert result["digit"] == 7


def test_tc_04_confidence_score():
    result = predict_digit("digit7.png")

    assert "confidence" in result
    assert result["confidence"] >= 0
    assert result["confidence"] <= 100


def test_tc_05_prediction_history(tmp_path):
    csv_file = tmp_path / "prediction_history.csv"

    save_prediction_history(
        csv_file,
        image_name="digit7.png",
        digit=7,
        confidence=95
    )

    history = pd.read_csv(csv_file)

    assert "image_name" in history.columns
    assert "predicted_digit" in history.columns
    assert "confidence" in history.columns
    assert "date" in history.columns

    assert history.iloc[0]["image_name"] == "digit7.png"
    assert history.iloc[0]["predicted_digit"] == 7
    assert history.iloc[0]["confidence"] == 95