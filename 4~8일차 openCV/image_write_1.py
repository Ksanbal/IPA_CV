# Read color image as gray and save it as jpg
import cv2 as cv

img = cv.imread('cat.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('img', img)
cv.waitKey()
cv.imwrite('gray cat.png', img)
