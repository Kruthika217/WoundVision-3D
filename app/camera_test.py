import cv2

from woundvision.acquisition.camera import Camera


def main() -> None:
    camera = Camera(camera_index=0)

    if not camera.open():
        print("ERROR: Could not open the camera.")
        print("Check camera permissions and make sure the camera is available.")
        return

    print("Camera opened successfully.")
    print("Press Q to quit.")

    try:
        while True:
            frame = camera.read()

            cv2.imshow("WoundVision 3D - Live Camera", frame)

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

    finally:
        camera.release()
        cv2.destroyAllWindows()

    print("Camera released.")


if __name__ == "__main__":
    main()