import sys

import cv2
import numpy as np
from matcher import Matcher


class Stitch:
    def __init__(self, left_image, right_image):
        self.matcher = Matcher()
        self.im_left = left_image
        self.im_right = right_image
        self.result = None

    def compute_matches(self):
        pass

    def merge(self):
        self.result = np.concatenate((self.im_left, self.im_right), axis=1)
        return self.result

    def _find_outer_corner(self, warp_affine):
        rows, cols, _ = np.nonzero(warp_affine)

        min_x_idx = np.argmin(cols)
        min_y_idx = np.argmin(rows)
        max_x_idx = np.argmax(cols)
        max_y_idx = np.argmax(rows)

        top_pnt = [cols[min_y_idx], rows[min_y_idx]]
        left_pnt = [cols[min_x_idx], rows[min_x_idx]]
        right_pnt = [cols[max_x_idx], rows[max_x_idx]]
        bottom_pnt = [cols[max_y_idx], rows[max_y_idx]]

        return top_pnt, right_pnt, bottom_pnt, left_pnt

    def transform(self):
        pts1 = np.float32([[180, 450], [5, 116], [338, 396]])
        pts2 = np.float32([[205, 370], [618, 126], [311, 407]])
        matrix = cv2.getAffineTransform(pts1, pts2)
        cols, rows, ch = self.im_right.shape

        warped_affine = cv2.warpAffine(self.im_right, matrix, (rows * 2, cols * 2))
        top_pnt, right_pnt, bottom_pnt, left_pnt = self._find_outer_corner(warped_affine)

        return warped_affine[top_pnt[1]:bottom_pnt[1], left_pnt[0]:right_pnt[0]]

    @classmethod
    def line_through(cls, point1, point2):
        y = point2[1] - ((point2[1] - point1[1]) / (point2[0] - point1[0])) * point2[0]
        pnt_x_0 = (0, int(y))
        x = point2[0] - point2[1] * ((point2[0] - point1[0]) / (point2[1] - point1[1]))
        pnt_y_0 = (int(x), 0)
        return pnt_x_0, pnt_y_0

    @classmethod
    def against_line(cls, pnt, pnt1, pnt2):
        """
        ### method 1: cross product
        """
        # v1 = [pnt2[0] - pnt1[0], pnt2[1] - pnt1[1]]
        # v2 = [pnt[0] - pnt1[0], pnt[1] - pnt1[1]]
        # r = np.cross(v1, v2)

        """
        ### method 2: algebra mathematical 
        """
        r = (pnt1[1] - pnt2[1]) * pnt[0] + (pnt2[0] - pnt1[0]) * pnt[1] + pnt1[0] * pnt2[1] - pnt2[0] * pnt1[1]
        return r

    def split_image_1(self, image, point1=(618, 126), point2=(254, 388)):
        pnt1, pnt2 = self.line_through(point1, point2)
        cv2.line(image, pnt1, pnt2, (0, 255, 0), 2)
        cv2.imshow('line', image)

    def split_image(self):
        pnt1, pnt2 = self.line_through((618, 126), (254, 388))
        h, w = self.im_left.shape[:2]
        for x in range(w):
            for y in range(h):
                if self.against_line((x, y), pnt1, pnt2) > 0:
                    self.im_left[y, x] = (255, 255, 255)

        pnt1, pnt2 = self.line_through((5, 116), (267, 424))

        h, w = self.im_right.shape[:2]
        for x in range(w):
            for y in range(h):
                if self.against_line((x, y), pnt1, pnt2) < 0:
                    self.im_right[y, x] = (255, 255, 255)

    def stitch(self):
        # self.split_image_1(self.im_left)
        self.split_image()
        # wraped = self.transform()
        # matcher = Matcher()

        # H = matcher.match(self.im_left, wraped)

        # print("Homography is : ", H)

        # cv2.imshow("warped", wraped)
        # cv2.waitKey(0)
        return None

    def imshow(self):
        cv2.imshow("left image", self.im_left)
        cv2.imshow("right Image", self.im_right)
        cv2.waitKey(0)


def read_images_from_file(file_paths='images.txt'):
    fp = open(file_paths, 'r')
    filenames = [each.rstrip('\r\n') for each in fp.readlines()]
    print(filenames)
    images = [cv2.resize(cv2.imread(each), (640, 480)) for each in filenames]
    return images


if __name__ == '__main__':
    try:
        args = sys.argv[1]
    except:
        args = "files_1.txt"

    image_list = read_images_from_file(args)

    s = Stitch(image_list[0], image_list[1])
    result = s.stitch()
    s.imshow()
    # cv2.namedWindow('result', cv2.WINDOW_AUTOSIZE)

    # cv2.imshow('result', result)
    cv2.waitKey(0)
    print("done")
    print("image written")
    cv2.destroyAllWindows()
