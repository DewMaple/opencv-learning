import cv2

from utils import find_image

image_path = find_image('girls_01.jpg')
img = cv2.imread(image_path)
cv2.imshow('girls_01', img)

# res = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
res = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

cv2.imshow('zoom_in', res)

height, width = img.shape[:2]
res = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_LINEAR)

print(res)

cv2.imshow('zoom_out', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
