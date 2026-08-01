import cv2

VIDEO_PATH = "videos/sample.mp4"

cap = cv2.VideoCapture(VIDEO_PATH)

success, frame = cap.read()

if not success:
    print("Failed to read frame")
    cap.release()
    exit()

# # ----------------------------
# # Resize Dimensions
# # ----------------------------

# new_width = 400
# new_height = 300

# # ----------------------------
# # Different Algorithms
# # ----------------------------

# nearest = cv2.resize(frame, (new_width, new_height), interpolation=cv2.INTER_NEAREST)

# bilinear = cv2.resize(frame, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

# bicubic = cv2.resize(frame, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

# lanczos = cv2.resize(frame, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)

# Crop a very small ROI
roi = frame[150:200, 250:300]

nearest = cv2.resize(roi, (600, 600), interpolation=cv2.INTER_NEAREST)

bilinear = cv2.resize(roi, (600, 600), interpolation=cv2.INTER_LINEAR)

bicubic = cv2.resize(roi, (600, 600), interpolation=cv2.INTER_CUBIC)

lanczos = cv2.resize(roi, (600, 600), interpolation=cv2.INTER_LANCZOS4)

cv2.imshow("Original", frame)
cv2.imshow("Nearest", nearest)
cv2.imshow("Bilinear", bilinear)
cv2.imshow("Bicubic", bicubic)
cv2.imshow("Lanczos", lanczos)

cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
