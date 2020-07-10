# 전체 밝기는 그대로 유지하면서 대비 높이기
# 평균 밝기를 유지하기 위해 평균을 기준으로 평균보다 낮은 값은 더 낮게, 큰 값은 더 높게 처리한다.
# 1. 평균이 0이 되도록 한다. f-m
# 2. scale을 곱해 차이를 키워준다. scale*(f-m)
# 3. 다시 원래 평균의 위치로 옯겨준다. sacle*(f-m)+m
# (img0-mean) * scale + mean -> img0 * scale - mean * scale +mean -> img0 * scale + mean * (1 - scale)

import cv2 as cv
import numpy as np

img0 = cv.imread('cat.jpg')
mean = np.zeros(img0.shape, np.uint8)   # 이미지와 같은 차원
mean[:,:] = np.mean(img0, (0,1))  # 평균을 구하는 차원을 지정

scale = 1.5
img1 = cv.addWeighted(img0, scale, mean, 1-scale, 0)

cv.imshow('img0', img0)
cv.imshow('mean', mean)
cv.imshow('img1', img1)

cv.waitKey()

