import cv2
import os
import numpy as np

# Addition
# x = np.uint8([250])
# y = np.uint8([100])
#
# print(cv2.add(x, y))
# print(x + y)
#
# cv2_path = os.path.join(os.path.dirname(__file__), '../resources/cv2-logo.png')
# ml_path = os.path.join(os.path.dirname(__file__), '../resources/ml-logo.png')
# cv2_img = cv2.imread(cv2_path)
# ml_img = cv2.imread(ml_path)
# addition = cv2.add(cv2_img, ml_img)
# print(addition)
#
# dst = cv2.addWeighted(cv2_img, 0.6, ml_img, 0.4, 40)
#
# cv2.imshow('img', dst)
# cv2.waitKey(0)

# Bitwise
# Load two images
girls_path = os.path.join(os.path.dirname(__file__), '../resources/girls.jpg')
cv2_path = os.path.join(os.path.dirname(__file__), '../resources/cv2-logo.png')
img1 = cv2.imread(girls_path)
img2 = cv2.imread(cv2_path)

# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]
not_roi = cv2.bitwise_not(roi)
print(roi)
print(not_roi)
cv2.imshow('roi', not_roi)

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi, roi)
cv2.imshow('img1_bg', mask_inv)
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
