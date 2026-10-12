import cv2

from woundvision.acquisition.camera import Camera
from woundvision.quality.image_quality import ImageQualityAnalyzer


def main() -> None:
    camera = Camera(camera_index=0)
    analyzer = ImageQualityAnalyzer()

    if not camera.open():
        print("ERROR: Could not open the camera.")
        print("Check camera permissions and make sure the camera is available.")
        return

    print("WoundVision 3D - Live Camera Quality Monitor")
    print("Press Q to quit.")

    try:
        while True:
            frame = camera.read()
            result = analyzer.analyze(frame)

            display_frame = frame.copy()

            if result["quality_ok"]:
                status_color = (0, 200, 0)
            else:
                status_color = (0, 165, 255)

            lines = [
                f"Quality: {result['status']}",
                f"Resolution: {result['width']} x {result['height']}",
                f"Brightness: {result['brightness']:.1f}",
                f"Contrast: {result['contrast']:.1f}",
                f"Sharpness: {result['sharpness']:.1f}",
            ]

            y_position = 30

            for index, line in enumerate(lines):
                color = (
                    status_color
                    if index == 0
                    else (255, 255, 255)
                )

                cv2.putText(
                    display_frame,
                    line,
                    (15, y_position),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.65,
                    color,
                    2,
                    cv2.LINE_AA,
                )

                y_position += 30

            if result["warnings"]:
                warning_text = result["warnings"][0]

                cv2.putText(
                    display_frame,
                    warning_text,
                    (15, y_position + 5),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.55,
                    (0, 165, 255),
                    2,
                    cv2.LINE_AA,
                )

            cv2.imshow(
                "WoundVision 3D - Live Camera Quality",
                display_frame,
            )

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

    except KeyboardInterrupt:
        print("\nCamera monitor stopped.")

    finally:
        camera.release()
        cv2.destroyAllWindows()

    print("Camera released.")


if __name__ == "__main__":
    main()