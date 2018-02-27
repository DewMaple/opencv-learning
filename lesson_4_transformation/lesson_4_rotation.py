import cv2
import numpy as np

from utils import find_image

image_path = find_image('girls_01.jpg')
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape

M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)

res = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('90 degree', res)

M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 60, 0.5)
res = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('60 degree, with half scalar', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
