import cv2


class Camera:
    """Simple wrapper around an OpenCV camera device."""

    def __init__(self, camera_index: int = 0):
        self.camera_index = camera_index
        self.capture = None

    def open(self) -> bool:
        """Open the camera device."""
        self.capture = cv2.VideoCapture(self.camera_index)

        if not self.capture.isOpened():
            self.capture.release()
            self.capture = None
            return False

        return True

    def read(self):
        """Read one frame from the camera."""
        if self.capture is None:
            raise RuntimeError("Camera is not open.")

        success, frame = self.capture.read()

        if not success:
            raise RuntimeError("Failed to read frame from camera.")

        return frame

    def release(self) -> None:
        """Release the camera device."""
        if self.capture is not None:
            self.capture.release()
            self.capture = None

    def is_open(self) -> bool:
        """Return whether the camera is currently open."""
        return self.capture is not None and self.capture.isOpened()