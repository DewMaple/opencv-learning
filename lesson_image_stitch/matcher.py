import cv2
import numpy as np


class Matcher:
    def __init__(self, detector='orb'):
        self.descriptor = detector.lower()

        if detector == 'sift':
            self.detector = cv2.xfeatures2d.SIFT_create()
        elif detector == 'surf':
            self.detector = cv2.xfeatures2d.SURF_create(400)
        else:
            self.detector = cv2.ORB_create()

    # def calculate_matches(self, des1, des2):
    #     bf = cv2.BFMatcher()
    #     matches = bf.knnMatch(des1, des2, k=2)
    #     good = []
    #     for m, n in matches:
    #         if m.distance < 0.75 * n.distance:
    #             good.append([m])
    #     return matches

    def match(self, im1, im2, direction=None):
        im_feature1 = self.get_features(im1)
        im_feature2 = self.get_features(im2)

        print("Direction : ", direction)
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        matches = bf.match(im_feature1['des'], im_feature2['des'])

        if len(matches) > 4:
            points_current = im_feature1['kp']
            points_pre = im_feature2['kp']

            matched_pnt_current = np.float32([points_current[i.queryIdx].pt for i in matches])
            matched_pnt_pre = np.float32([points_pre[i.trainIdx].pt for i in matches])

            H, S = cv2.findHomography(matched_pnt_current, matched_pnt_pre, cv2.RANSAC, 4)
            print(S)
            print(type(H))
            for h, s in zip(H, S):
                print(s)
            return H
        return None

    def get_features(self, im):
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        kp, des = self.detector.detectAndCompute(gray, None)
        return {'kp': kp, 'des': des}
