import cv2
import numpy as np

img = np.zeros((300, 300, 3), np.uint8)

polygon1 = cv2.ellipse2Poly((150, 150), (80, 10), 0, 0, 360, 1)
polygon2 = cv2.ellipse2Poly((150, 150), (40, 20), 90, 0, 360, 1)
# canvas = img.copy()

cv2.fillConvexPoly(img, polygon1, [0, 0, 255])
cv2.fillConvexPoly(img, polygon2, [0, 255, 0])
#
# img = cv2.addWeighted(img, 0.4, canvas, 0.6, 0)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#
# cv2.ellipse2Poly((int(mY), int(mX)), (int(length / 2), stickwidth), int(angle), 0, 360, 1)
