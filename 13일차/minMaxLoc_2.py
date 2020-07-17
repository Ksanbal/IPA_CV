# min max filter for color image

import cv2 as cv
import numpy as np


def minMaxFilterGray(img, kernel_size, flag):
    # kernel_size = 연산처리할 영역의 가로세로 사이즈
    # flag : 0이면 minFilter, 1이면 maxFilter
    kh = kw = kernel_size
    kh2, kw2 = kh//2, kw//2 # 커널의 중심에서 커널 끝까지의 거리

    dst = np.zeros(img.shape, img.dtype)

    for i in range(dst.shape[0]):       # dst의 세로
        for j in range(dst.shape[1]):   # dst의 가로
            roi = img[max(i-kh2, 0):i+kh2+1, max(j-kw2, 0):j+kw2+1]
            minVal, maxVal, _, _ = cv.minMaxLoc(roi)
            if flag == 0:
                dst[i, j] = minVal
            else:
                dst[i, j] = maxVal

    return dst


def minMaxFilter(img, kernel_size, flag):
    if len(img.shape) == 2:
        return minMaxFilterGray(img, kernel_size, flag)

    # BGR
    B, G, R = cv.split(img)
    BGR2 = list()
    for i in (B,G,R):
        BGR2.append(minMaxFilterGray(i, kernel_size, flag))
    dst = cv.merge(BGR2)

    # HSV

    return dst


img = cv.imread('min_max.jpg', cv.IMREAD_COLOR)
minFiltered = minMaxFilter(img, 7, 0)
maxFiltered = minMaxFilter(img, 7, 1)

cv.imshow('img', img)
cv.imshow('min', minFiltered)
cv.imshow('max', maxFiltered)
cv.waitKey()