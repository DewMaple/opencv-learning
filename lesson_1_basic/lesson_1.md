# Basic Operations on Images

## imread
```
img = cv2.imread(image_file, cv2::ImreadModes)
```
Read an image to an array, which is a 'height  weight  channel' dimensional array,
also an array of (Blue, Green, Red) value
'3' represents the channel, for gray scale image, represents intensity

## shape
```
shape = img.shape
```
Tuple of rows, columns, and channels, example `shape`: (342, 548, 3)

## size
```
size = img.size
```
Total number of pixels, example `size`: 562248

## image data type
```
dtype = img.dtype
```
Image data type, example `dtype`: uint8, float32, etc

## access pixel
```
px = img[100, 120]
```
Height 100, width 120, pixels, (BGR)/(Density)

## access specific VALUE of (BGR)
```
blue = img[100, 120, 0]  # height 100, width 120, blue value
green = img[100, 120, 1]  # height 100, width 120, green value
red = img[100, 120, 2]  # height 100, width 120, red value
```

## access position
```
im = img[100:200, 120:220]
```
Height from 100 to 200, weight from 120 to 220

## copy pixels from one region to another
```
ball = img[220:280, 322:382]
img[23:83, 100:160] = ball
```
Put the `img` region of `row 220 to 280, column 322 to 382`, to the region
of `row 23 to 83, column 100 to 160`, the two region must be the same shape

## split
```
b, g, r = cv2.split(img) # or
b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]
```
This operation is very expensive, `b`, `g`, `r` will be 2 dimensional array

## merge
```
im = cv2.merge(b, g, r)
```
Merge matrices into one,  matrices must have the same size and depth




