import cv2

VIDEO_PATH = "videos/sample.mp4"

cap = cv2.VideoCapture(VIDEO_PATH)

success, frame = cap.read()

if not success:
    print("Failed to read frame")
    cap.release()
    exit()

# ---------------------------------
# Image Information
# ---------------------------------

height, width, channels = frame.shape

print(f"Width  : {width}")
print(f"Height : {height}")

# ---------------------------------
# Rotation Parameters
# ---------------------------------

center = (width / 2, height / 2)

angle = 45

scale = 1.0

# ---------------------------------
# Create Rotation Matrix
# ---------------------------------

rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

# ---------------------------------
# Rotate Image
# ---------------------------------

# rotated = cv2.warpAffine(frame, rotation_matrix, (width, height))
rotated = cv2.warpAffine(
    frame, rotation_matrix, (width, height), borderValue=(255, 255, 255)
)

cv2.imshow("Original", frame)
cv2.imshow("Rotated", rotated)

cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
