import argparse

import cv2
import imutils

from utils import find_image


class Stitcher:
    def stitch(self, images, key_points):
        image_1 = cv2.imread(images[0])
        image_2 = cv2.imread(images[1])
        sift = cv2.xfeatures2d.SIFT_create()
        kp1, des1 = sift.detectAndCompute(image_1, None)
        kp2, des2 = sift.detectAndCompute(image_2, None)
        print(kp1)
        print(kp2)


def resize(image, width):
    (h, w) = image.shape[:2]
    r = width / float(w)
    dim = (width, int(h * r))
    return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)


if __name__ == '__main__':
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-f", "--first", help="path to the first image")
    # ap.add_argument("-s", "--second", help="path to the second image")
    #
    # args = vars(ap.parse_args())
    args = {"first": find_image('mpv-shot0001.jpg'), 'second': find_image('mpv-shot0002.jpg')}

    print(args)
    imageA = cv2.imread(args["first"])
    imageB = cv2.imread(args["second"])
    imageA = resize(imageA, width=800)
    imageB = resize(imageB, width=800)
    imageB = imutils.rotate(imageB, -12)
    # show the images
    cv2.imshow("Image A", imageA)
    cv2.imshow("Image B", imageB)
    # cv2.imshow("Keypoint Matches", vis)
    # cv2.imshow("Result", result)
    cv2.waitKey(0)
