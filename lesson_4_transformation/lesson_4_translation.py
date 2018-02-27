import cv2
import numpy as np

from utils import find_image

image_path = find_image('girls_01.jpg')
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape
M = np.float32([[1, 0, 100], [0, 1, 50]])
res = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('xy direction', res)

M = np.float32([[1, 0, 0], [0, 1, 200]])
res = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('y direction', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
