# img의 Red 제거하기
import cv2 as cv

img = cv.imread('cat.jpg', cv.IMREAD_UNCHANGED)

img[:, :, 2] = 0

cv.imshow('img', img)
cv.waitKey()