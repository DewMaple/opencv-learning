import numpy as np
import sys

import cv2
import os
from img_utils.files import images_in_dir
from img_utils.images import put_text


def is_blur_laplacian(image, threshold=100):
    laplacian_variance = cv2.Laplacian(image, cv2.CV_64F).var()

    return laplacian_variance < threshold, laplacian_variance


def is_blur_sobel(image, threshold=0.0003):
    gx = cv2.Sobel(image, cv2.CV_64F, 1, 0)
    gy = cv2.Sobel(image, cv2.CV_64F, 0, 1)
    nx = cv2.norm(gx)
    ny = cv2.norm(gy)
    sum_sqrt = nx * nx + ny * ny
    h, w = image.shape[:2]
    sharpness = 1. / (sum_sqrt / (h * w) + 1e-6)
    return sharpness > threshold, sharpness


def is_blur_sobel_2(image, threshold=0.0003):
    gx = cv2.Sobel(image, cv2.CV_32F, 1, 0, 3)
    gy = cv2.Sobel(image, cv2.CV_32F, 0, 1, 3)
    magnitude = cv2.magnitude(gx, gy)
    print(sum(magnitude)[0])
    print(sum(magnitude).var())


def fft(image):
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)

    # rows, cols = image.shape[:2]
    # crow, ccol = rows // 2, cols // 2
    # fshift[crow - 50:crow + 50, ccol - 50:ccol + 50] = 0
    # fshift[:, :] = 0
    f_ishift = np.fft.ifftshift(fshift)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)
    print(img_back.var())
    # cv2.imshow('im', img_back)
    # cv2.waitKey(0)
    return True, img_back.var()


if __name__ == '__main__':
    args = sys.argv
    images_dir = args[1]
    output_dir = args[2]

    image_files = images_in_dir(images_dir)
    for im_f in image_files:
        im = cv2.imread(im_f)
        print(im_f)
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        cv2.G
        blurred, lap = fft(gray)
        img = put_text(im, 'B: {}'.format(blurred), (10, 20))
        img = put_text(img, 'L: {}'.format(lap), (10, 40))
        cv2.imwrite(os.path.join(output_dir, im_f.split(os.sep)[-1]), img)
