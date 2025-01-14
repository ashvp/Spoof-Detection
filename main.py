import cv2
from deepface import DeepFace
cap = cv2.VideoCapture(0)

print("Press 's' to capture the image and 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame. Exiting ...")
        break
    cv2.imshow('Camera', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        cv2.imwrite("image.jpg", frame)
        break
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

values = DeepFace.extract_faces(img_path="image.jpg", anti_spoofing=True)
try:
    if values[0]['is_real']:
        print("It is a Real Face.")
    else:
        print("It is a Spoofed Face.")
except:
    print("Please capture another image with better lighting.")