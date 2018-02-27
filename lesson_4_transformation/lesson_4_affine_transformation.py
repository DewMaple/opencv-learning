import cv2
import numpy as np

from utils import find_image

image_path = find_image('girls_01.jpg')
img = cv2.imread(image_path)
rows, cols, channel = img.shape

pts_src = np.float32([[50, 50], [200, 50], [50, 200]])
pts_dst = np.float32([[10, 100], [200, 80], [100, 650]])

M = cv2.getAffineTransform(pts_src, pts_dst)
res = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('transformation by three points', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
