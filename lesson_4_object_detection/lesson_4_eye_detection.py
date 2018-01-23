import cv2
import os

eye_path = os.path.join(os.path.dirname(__file__), '../data/haarcascades_cuda/haarcascade_eye.xml')
eye_cascade = cv2.CascadeClassifier(eye_path)


def detect(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    return img


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if ret is True:
        detected = detect(frame)
        cv2.imshow('Face detection', detected)
    else:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
