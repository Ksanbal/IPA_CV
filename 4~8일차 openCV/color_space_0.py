# RGB를 다른 컬러 스페이스로 변경
import cv2 as cv

bgr = cv.imread('cat.jpg')
HSV = cv.cvtColor(bgr, cv.COLOR_BGR2HSV)
H, S, V = cv.split(HSV)

cv.imshow('bgr', bgr)
cv.imshow('H', H)
cv.imshow('S', S)
cv.imshow('V', V)
cv.waitKey()

cv.imwrite('cat-h.png', H)
cv.imwrite('cat-s.png', S)
cv.imwrite('cat-v.png', V)