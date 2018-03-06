import cv2
import numpy as np
from scipy import ndimage

from utils import find_image

kernel_3x3 = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
])

kernel_5x5 = np.array([
    [-1, -1, -1, -1, -1],
    [-1, 1, 2, 1, -1],
    [-1, 2, 4, 2, -1],
    [-1, 1, 2, 1, -1],
    [-1, -1, -1, -1, -1],
])
image_path = find_image('Katrina_Kaif.jpg')
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
k3 = ndimage.convolve(image, kernel_3x3)
k5 = ndimage.convolve(image, kernel_5x5)

blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow('blurred', blurred)
g_hpf = image - blurred
cv2.imshow('convolve_3x3', k3)
cv2.imshow('convolve_5x5', k5)
cv2.imshow('g_hpf', g_hpf)
cv2.waitKey(0)
cv2.destroyAllWindows()
