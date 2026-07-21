import cv2

VIDEO_PATH = "videos/sample.mp4"

cap = cv2.VideoCapture(VIDEO_PATH)

success, frame = cap.read()

if not success:
    print("Failed to read video")
    cap.release()
    exit()

# ----------------------------
# ROI Coordinates
# ----------------------------

x1 = 100
y1 = 250

x2 = 550
y2 = 300

# Crop ROI
roi = frame[y1:y2, x1:x2]

# Draw rectangle on original frame
cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow("Original Frame", frame)
cv2.imshow("ROI", roi)

cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
