import cv2 as cv
image = cv.imread("test.jpg")
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
inverted = 255 - gray_image
blur = cv.GaussianBlur(inverted, (21, 21), 0)
invertedblur = 255 - blur
sketch = cv.divide(gray_image, invertedblur, scale=256.0)
cv.imwrite("sketch_img.png", sketch)
cv.imshow("image", sketch)
