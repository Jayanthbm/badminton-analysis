import cv2

VIDEO_PATH = "videos/sample.mp4"

cap = cv2.VideoCapture(VIDEO_PATH)

success, frame = cap.read()

if not success:
    print("Failed to read video")
    cap.release()
    exit()

# -------------------------
# ROI Coordinates
# -------------------------

x1 = 100
y1 = 100

x2 = 400
y2 = 350

# ROI (View)
roi = frame[y1:y2, x1:x2].copy()

# Paint ROI completely red
roi[:] = (0, 0, 255)

cv2.imshow("Frame", frame)
cv2.imshow("ROI", roi)

cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
