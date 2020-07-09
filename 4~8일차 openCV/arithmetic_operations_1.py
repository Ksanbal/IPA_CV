# Add two images
import cv2 as cv

img0 = cv.imread('add1.jpg', cv.IMREAD_UNCHANGED)
img1 = cv.imread('add2.jpg', cv.IMREAD_UNCHANGED)

# numpy 연산
np_img = img0+img1

# openCV 연산
cv_img = cv.add(img0, img1)

cv.imshow('np_img', np_img)
cv.imshow('cv_img', cv_img)

cv.waitKey()