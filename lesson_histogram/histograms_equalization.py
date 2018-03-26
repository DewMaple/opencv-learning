import sys

import cv2
import numpy as np
import os

from utils import images_in_dir

if __name__ == '__main__':
    args = sys.argv
    if len(args) < 3:
        print("Usage: python histograms_equalization.py input_dir output_dir")
        exit(1)

    input_dir = args[1]
    output_dir = args[2]
    images = images_in_dir(input_dir)
    for im in images:
        fname = im.split(os.sep)[-1]
        gray_im = cv2.imread(im, 0)
        hist = cv2.equalizeHist(gray_im)
        result = np.hstack((gray_im, hist))
        filename = os.path.join(output_dir, fname)
        cv2.imwrite(filename, result)
