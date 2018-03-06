import cv2
import numpy as np

from utils import find_image

image_path = find_image('ml-logo.png')
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(gray, 50, 200)

min_line_length = 20
max_line_gap = 50

lines = cv2.HoughLinesP(edge, 1, np.pi / 180, 50, None, min_line_length, max_line_gap)

for x1, y1, x2, y2 in lines[0]:
    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 1)

cv2.imshow('edge', edge)
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
