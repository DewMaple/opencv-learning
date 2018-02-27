import cv2
import numpy as np

from utils import find_image

image_path = find_image('girls_01.jpg')
img = cv2.imread(image_path)
cv2.imshow('origin', img)
rows, cols, channel = img.shape

pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
M = cv2.getPerspectiveTransform(pts1, pts2)
res = cv2.warpPerspective(img, M, (cols, rows))

cv2.imshow('transformation by 4 points', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
