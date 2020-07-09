# 최대 3초동안 그림을 보여주 키 입력을 프린트

import cv2 as cv

img = cv.imread('cat.jpg', cv.IMREAD_UNCHANGED)

cv.imshow('img', img)
key = cv.waitKey(3000)  # 시간의 단위는 밀리세컨드
print('key = ', key)