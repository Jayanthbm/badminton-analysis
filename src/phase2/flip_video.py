import cv2

VIDEO_PATH = "videos/sample.mp4"

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print("Failed to open video")
    exit()

while True:

    success, frame = cap.read()

    if not success:
        print("End of video")
        break

    # Horizontal Flip
    flipped_frame = cv2.flip(frame, 1)

    cv2.imshow("Original", frame)
    cv2.imshow("Horizontal Flip", flipped_frame)

    key = cv2.waitKey(30)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
