import os

import cv2

front_face_path = os.path.join(os.path.dirname(__file__), '../data/haarcascades/haarcascade_frontalface_default.xml')
eye_path = os.path.join(os.path.dirname(__file__), '../data/haarcascades/haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier(front_face_path)
eye_cascade = cv2.CascadeClassifier(eye_path)


def detect(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

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
