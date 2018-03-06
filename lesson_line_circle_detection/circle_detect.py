import cv2
import numpy as np

from utils import find_image

image_path = find_image('ml-logo.png')
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11,11), 2)

circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 40,
                           param1=50, param2=30, minRadius=0, maxRadius=50)
circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    # draw the outer circle
    cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)

cv2.imshow('edge', blurred)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
