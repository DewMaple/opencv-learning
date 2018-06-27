#!/usr/bin/env python

import cv2
import numpy as np

# Read Image
im = cv2.imread("headPose.jpg");
size = im.shape

# 2D image points. If you change the image, you need to change vector
image_points = np.array([
    (359, 391),  # Nose tip
    (467, 311),  # Left eye left corner
    (352, 311),  # Right eye right corne
    (642, 372),  # Left ear corner
    (314, 346)  # Right ear corner
], dtype="double")

# 3D model points.
model_points = np.array([
    (0.55592, 6.5629, -25.944448),  # Nose tip
    (28.76499, -35.484287, -1.172675),  # Left eye left corner
    (-28.272964, -35.134495, -0.147273),  # Right eye right corne
    (70.486404, -11.666193, 44.142567),  # Left ear corner
    (-72.77502, -10.949766, 45.909405)  # Right ear corner
])

# Camera internals

focal_length = size[1]
center = (size[1] / 2, size[0] / 2)
camera_matrix = np.array(
    [[focal_length, 0, center[0]],
     [0, focal_length, center[1]],
     [0, 0, 1]], dtype="double"
)

print("Camera Matrix :\n {0}".format(camera_matrix))

dist_coeffs = np.zeros((4, 1))  # Assuming no lens distortion
(success, rotation_vector, translation_vector) = cv2.solvePnP(model_points, image_points, camera_matrix, dist_coeffs)

print("Rotation Vector:\n {0}".format(rotation_vector))

print("Translation Vector:\n {0}".format(translation_vector))

# Project a 3D point (0, 0, 1000.0) onto the image plane.
# We use this to draw a line sticking out of the nose

# axis = np.float32([[3, 0, 0], [0, 3, 0], [0, 0, -3]]).reshape(-1, 3)
axis = np.array([(0.0, 0.0, 1000.0)])
(nose_end_point2D, jacobian) = cv2.projectPoints(axis, rotation_vector, translation_vector,
                                                 camera_matrix, dist_coeffs)

for p in image_points:
    cv2.circle(im, (int(p[0]), int(p[1])), 3, (0, 0, 255), -1)

p1 = (int(image_points[0][0]), int(image_points[0][1]))
p2 = (int(nose_end_point2D[0][0][0]), int(nose_end_point2D[0][0][1]))

cv2.line(im, p1, p2, (255, 0, 0), 2)

# Display image
cv2.imshow("Output", im)
cv2.waitKey(0)
