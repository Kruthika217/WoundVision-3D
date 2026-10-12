import cv2
import numpy as np


class ImageQualityAnalyzer:
    """Measure basic technical quality indicators in an image frame."""

    def __init__(
        self,
        min_width: int = 640,
        min_height: int = 480,
        min_brightness: float = 40.0,
        max_brightness: float = 220.0,
        min_sharpness: float = 80.0,
    ):
        self.min_width = min_width
        self.min_height = min_height
        self.min_brightness = min_brightness
        self.max_brightness = max_brightness
        self.min_sharpness = min_sharpness

    def analyze(self, frame: np.ndarray) -> dict:
        """Analyze an OpenCV BGR or grayscale image."""

        if frame is None:
            raise ValueError("Frame cannot be None.")

        if not isinstance(frame, np.ndarray):
            raise TypeError("Frame must be a NumPy array.")

        if frame.size == 0:
            raise ValueError("Frame cannot be empty.")

        if frame.ndim == 2:
            gray = frame
        elif frame.ndim == 3 and frame.shape[2] == 3:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        else:
            raise ValueError(
                "Frame must be a grayscale image or a 3-channel BGR image."
            )

        height, width = gray.shape

        brightness = float(np.mean(gray))
        contrast = float(np.std(gray))
        sharpness = float(cv2.Laplacian(gray, cv2.CV_64F).var())

        resolution_ok = (
            width >= self.min_width and height >= self.min_height
        )
        brightness_ok = (
            self.min_brightness <= brightness <= self.max_brightness
        )
        sharpness_ok = sharpness >= self.min_sharpness

        quality_ok = resolution_ok and brightness_ok and sharpness_ok

        warnings = []

        if not resolution_ok:
            warnings.append("Resolution too low")

        if not brightness_ok:
            warnings.append("Lighting may be too dark or too bright")

        if not sharpness_ok:
            warnings.append("Image may be blurry")

        return {
            "width": width,
            "height": height,
            "brightness": brightness,
            "contrast": contrast,
            "sharpness": sharpness,
            "resolution_ok": resolution_ok,
            "brightness_ok": brightness_ok,
            "sharpness_ok": sharpness_ok,
            "quality_ok": quality_ok,
            "status": "GOOD" if quality_ok else "WARNING",
            "warnings": warnings,
        }