import cv2

VIDEO_PATH = "videos/sample.mp4"

cap = cv2.VideoCapture(VIDEO_PATH)

success, frame = cap.read()

if not success:
    print("Failed to read frame")
    cap.release()
    exit()

horizontal = cv2.flip(frame, 1)
vertical = cv2.flip(frame, 0)
both = cv2.flip(frame, -1)

cv2.imshow("Original", frame)
cv2.imshow("Horizontal", horizontal)
cv2.imshow("Vertical", vertical)
cv2.imshow("Both", both)

cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
