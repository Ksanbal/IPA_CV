import cv2 as cv
import numpy as np

img1 = np.zeros((300, 300), np.uint8)
img2 = np.zeros((300, 300), np.uint8)
mask = np.zeros((300, 300), np.uint8)

cv.circle(img1, (150, 150), 100, 255, -1)
cv.rectangle(img2, (0, 0), (150, 300), 255, -1)
cv.rectangle(mask, (0, 0), (300, 150), 128, -1)

cv.imshow('img1', img1)
cv.imshow('img2', img2)
cv.imshow('mask', mask)

# 논리연산
# OR
cv.imshow('img1_or_img2', cv.bitwise_or(img1, img2, mask=mask))
# XOR
cv.imshow('img1_xor_img2', cv.bitwise_xor(img1, img2, mask=mask))
# NOT
cv.imshow('img1_not', cv.bitwise_not(img1, mask=mask))

cv.waitKey()