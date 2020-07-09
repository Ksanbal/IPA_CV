import cv2 as cv
import numpy as np

img1 = np.zeros((300, 300), np.uint8)
img2 = np.zeros((300, 300), np.uint8)
mask = np.zeros((300, 300), np.uint8)

# 원 그리기 params = 이미지, 중심, 반지름, 색, 선의 굵기(0보다 작아지면 속을 채우게 된다)
cv.circle(img1, (150, 150), 100, 255, -1)
# 사각형 그리기 params = 이미지, 왼쪽 위 끝의 좌표, 오른쪽 아래 끝의 좌표, 색, 선의 굵기
cv.rectangle(img2, (0, 0), (150, 300), 255, -1)
cv.rectangle(mask, (0, 0), (300, 150), 128, -1)

cv.imshow('img1', img1)
cv.imshow('img2', img2)
cv.imshow('mask', mask)

# 논리연산
# bit 단위로 비교해 논리연산을 수행하게 된다.
# AND
cv.imshow('img1_and_img2', cv.bitwise_and(img1, img2))  # 색이 겹쳐져 있는 곳을 표시
cv.imshow('img1_and_img2_mask', cv.bitwise_and(img1, img2, mask=mask)) # mask에 값이 있는 픽셀(8bit)에서만 연산을 할 수 있도록 지정
                                                                       # 검정으로 채워진 임시이미지를 나두고, mask에 해당하는 값만 연산
                                                                       # mask는 결과 필터링이 아닌, mask의 값이 있는 부분만 연산
dst_img = np.full((300,300), 127, dtype=np.uint8)   # dst = 임시로 생성되는 이미지를 지정
cv.imshow('img1_and_img2_dst_mask', cv.bitwise_and(img1, img2, dst=dst_img, mask=mask))

cv.waitKey()