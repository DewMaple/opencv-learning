import cv2
import glob

image_files = glob.glob('../resources/nuts.jpg')

for im_f in image_files:
    im = cv2.imread(im_f, cv2.IMREAD_GRAYSCALE)
    # ret, thresh = cv2.threshold(im, 200, 255, 0)
    edged = cv2.Canny(im, 30, 200)
    cv2.imshow('thresh', edged)
    im2, contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))
    print(contours[2].shape)

    cv2.drawContours(im, contours, -1, (0, 255, 0), 3)
    # cv2.solvePnP()

    cv2.imshow('contours', im)
    cv2.waitKey(0)
cv2.destroyAllWindows()
