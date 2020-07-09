# esc를 누르면 사진을 끄는 프로그램 작성

import cv2 as cv

img = cv.imread('cat.jpg', cv.IMREAD_UNCHANGED)

cv.imshow('img', img)

while True:
    key = cv.waitKey()
    if key == 27:
        print('종료합니다.')
        break