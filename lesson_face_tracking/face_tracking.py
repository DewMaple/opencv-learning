import cv2
import os

front_face_path = os.path.join(os.path.dirname(__file__), '../data/haarcascades/haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(front_face_path)


def create_tracker(tracker_type=1):
    tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'CSRT', 'MOSSE']
    if tracker_type > len(tracker_types):
        tracker_type = 0
    tracker_type = tracker_types[tracker_type]

    if tracker_type == 'BOOSTING':
        tracker = cv2.TrackerBoosting_create()
    elif tracker_type == 'MIL':
        tracker = cv2.TrackerMIL_create()
    elif tracker_type == 'KCF':
        tracker = cv2.TrackerKCF_create()
    elif tracker_type == 'TLD':
        tracker = cv2.TrackerTLD_create()
    elif tracker_type == 'MEDIANFLOW':
        tracker = cv2.TrackerMedianFlow_create()
    elif tracker_type == 'GOTURN':
        tracker = cv2.TrackerGOTURN_create()
    elif tracker_type == 'CSRT':
        tracker = cv2.TrackerCSRT_create()
    elif tracker_type == 'MOSSE':
        tracker = cv2.TrackerMOSSE_create()
    return tracker


def detect_face(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    print('faces: {}'.format(faces))
    # bboxes = []
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # bboxes.append((x, y, x + w, y + h))
    # if len(faces) > 0:
    #     cv2.imshow('image', image)
    #     k = cv2.waitKey(0) & 0xff
    #     if k == 27:
    #         cv2.destroyWindow('image')
    return faces, image


def main():
    cap = cv2.VideoCapture(0)
    tracking = False
    tracker = None
    while True:
        ret, frame = cap.read()
        if not ret:
            print('Read camera Error!!!')
            break
        if not tracking:
            faces, img = detect_face(frame)
            if len(faces) < 1:
                continue
            tracker = create_tracker(7)
            tracking = tracker.init(frame, tuple(faces[0]))
            continue

        tracking, bbox = tracker.update(frame)
        print('Tracking: {}'.format(tracking))

        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
        cv2.imshow("Tracking", frame)

        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
