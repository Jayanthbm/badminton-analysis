import cv2

video_path = "videos/sample.mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    success, frame = cap.read()

    if not success:
        break

    cv2.circle(frame, (175, 200), 6, (0, 0, 255), -1)
    cv2.imshow("Badminton Analysis", frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
