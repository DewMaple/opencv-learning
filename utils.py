import cv2
import os

opencv_logo_path = os.path.join(os.path.dirname(__file__), 'resources/cv2-logo.png')
opencv_logo = cv2.imread(opencv_logo_path)
resized = cv2.resize(opencv_logo, (460, 259), interpolation=cv2.INTER_CUBIC)
cv2.imwrite('resized.png', resized)
