import cv2
import numpy as np
import os

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)

girls_path = os.path.join(os.path.dirname(__file__), '../resources/cv2-logo.png')

frame = cv2.imread(girls_path)

# Convert BGR to HSV
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv', hsv)
# define range of blue color in HSV
# lower_blue = np.array([110, 50, 50])
# upper_blue = np.array([130, 255, 255])
blue = np.uint8([[[0, 0, 255]]])
hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)

lower_blue = np.array([[hsv_blue[0][0][0] - 10, 100, 100]])
upper_blue = np.array([[hsv_blue[0][0][0] + 10, 255, 255]])
cv2.imshow('lower_blue', lower_blue)
# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(frame, frame, mask=mask)

cv2.imshow('frame', frame)
cv2.imshow('mask', mask)
cv2.imshow('res', res)

k = cv2.waitKey(0)
cv2.destroyAllWindows()
