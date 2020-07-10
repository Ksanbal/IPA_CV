# h,s,v 그림파일을 읽어서 원본 이미지 만들고 보여주기
import cv2 as cv

# 그레이스케일 그대로 읽어와야한다.
H = cv.imread('cat-h.png', cv.IMREAD_UNCHANGED)
S = cv.imread('cat-s.png', cv.IMREAD_UNCHANGED)
V = cv.imread('cat-v.png', cv.IMREAD_UNCHANGED)

HSV = cv.merge((H,S,V))
cv.imshow('HSV', HSV)

BGR = cv.cvtColor(HSV, cv.COLOR_HSV2BGR)
cv.imshow('BGR', BGR)

cv.waitKey()