# Arithmetic Operation on Images

## image add
```
x = np.uint8([250])
y = np.uint8([100])
xy = cv2.add(x, y)
xy = x + y
```
It's different that cv2.add and numpy addition, `cv2: [[255]]`, `numpy: [[94]]`

## image blend
```
dst = cv2.addWeighted(cv2_img, 0.6, ml_img, 0.4, 0)
```
dst = alpha * cv2_img + beta * ml_img + gamma

## bitwise
- Include AND, OR, NOT and XOR operations
- Highly used to extract any part of image