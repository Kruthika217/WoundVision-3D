import numpy as np
import pytest

from woundvision.quality.image_quality import ImageQualityAnalyzer


def test_quality_analyzer_returns_expected_fields():
    analyzer = ImageQualityAnalyzer()

    rng = np.random.default_rng(42)
    frame = rng.integers(
        0, 256, size=(480, 640, 3), dtype=np.uint8
    )

    result = analyzer.analyze(frame)

    expected_fields = {
        "width",
        "height",
        "brightness",
        "contrast",
        "sharpness",
        "resolution_ok",
        "brightness_ok",
        "sharpness_ok",
        "quality_ok",
        "status",
        "warnings",
    }

    assert expected_fields.issubset(result.keys())


def test_resolution_is_detected():
    analyzer = ImageQualityAnalyzer()
    frame = np.zeros((480, 640, 3), dtype=np.uint8)

    result = analyzer.analyze(frame)

    assert result["width"] == 640
    assert result["height"] == 480
    assert result["resolution_ok"] is True


def test_invalid_none_frame_is_rejected():
    analyzer = ImageQualityAnalyzer()

    with pytest.raises(ValueError, match="Frame cannot be None"):
        analyzer.analyze(None)


def test_empty_frame_is_rejected():
    analyzer = ImageQualityAnalyzer()

    with pytest.raises(ValueError, match="Frame cannot be empty"):
        analyzer.analyze(np.array([]))


def test_non_array_input_is_rejected():
    analyzer = ImageQualityAnalyzer()

    with pytest.raises(TypeError, match="NumPy array"):
        analyzer.analyze("not an image")


def test_grayscale_image_is_supported():
    analyzer = ImageQualityAnalyzer()
    frame = np.full((480, 640), 120, dtype=np.uint8)

    result = analyzer.analyze(frame)

    assert result["width"] == 640
    assert result["height"] == 480