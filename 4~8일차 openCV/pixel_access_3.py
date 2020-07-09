# Split each channels using cv2.split
import cv2 as cv

img = cv.imread('cat.jpg', cv.IMREAD_UNCHANGED)
b, g, r = cv.split(img, )

cv.imshow('img', img)
cv.imshow('b', b)
cv.imshow('g', g)
cv.imshow('r', r)
cv.waitKey()
