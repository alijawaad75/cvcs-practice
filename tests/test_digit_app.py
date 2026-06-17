import pandas as pd
from digit_app import (
    upload_image,
    preprocess_image,
    predict_digit,
    save_prediction_history
)


def test_tc_01_image_upload(tmp_path):
    target = tmp_path / "digit7.png"
    result = upload_image(str(target))
    assert result == True


def test_tc_02_image_preprocessing(tmp_path):
    target = tmp_path / "digit7.png"
    upload_image(str(target))
    result = preprocess_image(str(target))

    assert result["size"] == (28, 28)
    assert result["mode"] == "grayscale"
    assert result["normalized"] == True


def test_tc_03_digit_prediction(tmp_path):
    target = tmp_path / "digit7.png"
    upload_image(str(target))
    result = predict_digit(str(target))

    assert result["digit"] == 7


def test_tc_04_confidence_score(tmp_path):
    target = tmp_path / "digit7.png"
    upload_image(str(target))
    result = predict_digit(str(target))

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
