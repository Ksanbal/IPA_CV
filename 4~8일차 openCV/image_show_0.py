import cv2 as cv

img = cv.imread('cat.jpg', cv.IMREAD_UNCHANGED)     # 이미지를 흑백으로 바꾸거나 하는 변형없이 불러옴

cv.imshow('img', img)   # 이미지를 보여주는 함수
cv.waitKey()    # 키 입력때까지 종료를 기다림

