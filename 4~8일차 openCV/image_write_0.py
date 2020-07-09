# 이미지 생성 및 디스크에 파일로 저장
import cv2 as cv
import numpy as np

img = np.zeros((480, 640, 3), dtype=np.uint8)

cv.imshow('img', img)
cv.waitKey()
cv.imwrite('img.png', img) # openCV가 확장자에 맞게 저장을 실행함