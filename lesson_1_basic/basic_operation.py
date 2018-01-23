import cv2
import os

# def read():
img_path = os.path.join(os.path.dirname(__file__), '../resources/roi.jpg')
img = cv2.imread(img_path)
print(img.shape)
print(len(img[0, 0]))
print(img.size)
print(img.dtype)
print(img[100, 120])

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

ball = img[220:280, 322:382]
cv2.imshow('img', ball)
print(ball.shape)

img[23:83, 100:160] = ball
cv2.imshow('ball', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
