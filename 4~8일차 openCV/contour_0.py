# 도형을 둘러싼 라인을 감지

import cv2 as cv
import numpy as np

img = np.zeros((480,640,3), np.uint8)

cv.circle(img, (200,150), 80, (255,255,0), -1)
cv.circle(img, (500,150), 50, (255,0,0), -1)
cv.rectangle(img, (300,300), (500,400), (0,255,255), -1)

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 노란색과 하늘색만 감지하기 위해 파란색을 제거
_, img_thresh = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY)    # 임계값 -> 특정 값보다 크고 작음을 따져서 연산

contours, _ = cv.findContours(img_thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)   # 도형을 감지
print('contours : ', type(contours))
for c in contours:
    print(c.shape, c.dtype, cv.contourArea(c))

# for i in range(contours[0].shape[0]):
for i in range(500):
    cv.circle(img, (contours[0][i,0,0], contours[0][i,0,1]), 3, (0,255,0), -1)

cv.drawContours(img, contours, 1, (0,0,255), 3)

cv.imshow('img', img)
cv.imshow('img_gray', img_gray)
cv.imshow('img_thresh', img_thresh)
cv.waitKey()