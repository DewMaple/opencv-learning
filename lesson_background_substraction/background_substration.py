import cv2 as cv

cap = cv.VideoCapture('/Users/administrator/Documents/video/quantum_students.mp4')
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (1, 1))
fgbg = cv.bgsegm.createBackgroundSubtractorGMG()
while (1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel)
    cv.imshow('frame', fgmask)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()
