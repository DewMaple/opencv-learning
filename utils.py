import cv2
import os


def find_image(image_name):
    return os.path.join(os.path.dirname(__file__), 'resources/{}'.format(image_name))


def resize_image(image_name):
    opencv_logo_path = find_image(image_name)
    opencv_logo = cv2.imread(opencv_logo_path)
    resized = cv2.resize(opencv_logo, (460, 259), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite('resized.png', resized)
