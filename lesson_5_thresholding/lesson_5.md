# Thresholding

## Simple thresholding

Simple thresholding is that set a threshold value which the pixels in an
image greater than will be assigned to one value (maybe black), those less than
will be assigned to another value (maybe white). The function is cv2.threshold.
The image should be grayscale image
```
ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)
```

## Adaptive thresholding

What different from simple thresholding is that adaptive thresholding can set
threshold value in different region of an image, while simple threshold set
global threshold value.

```
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
```

## Otsu’s Binarization

It automatically calculates a threshold value from image histogram for a bimodal image.
(For images which are not bimodal, binarization won’t be accurate.)