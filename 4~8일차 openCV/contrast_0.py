import cv2 as cv

img0 = cv.imread('cat.jpg')
img1 = cv.addWeighted(img0, 1.5, img0, 0, 0)

cv.imshow('img0', img0)
cv.imshow('img1', img1)
cv.waitKey()