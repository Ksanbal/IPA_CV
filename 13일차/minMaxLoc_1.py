# min max filter

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
            # # write by ksanbal
            # j_start = j - kw2
            # j_last = j + kw2
            # i_start = i - kh2
            # i_last = i + kh2
            # if j_start < 0: j_start = 0
            # if i_start < 0: i_start = 0
            # if j_last > dst.shape[1]: j_last = dst.shape[1]
            # if i_last > dst.shape[0]: i_last = dst.shape[0]
            #
            # roi = img[i_start:i_last+1, j_start:j_last+1]
            #
            # minVal, maxVal, _, _ = cv.minMaxLoc(roi)
            # if flag:    # 최대값
            #     dst[i][j] = maxVal
            # else:       # 최소값
            #     dst[i][j] = minVal

            roi = img[max(i-kh2, 0):i+kh2+1, max(j-kw2, 0):j+kw2+1]
            minVal, maxVal, _, _ = cv.minMaxLoc(roi)
            if flag == 0:
                dst[i, j] = minVal
            else:
                dst[i, j] = maxVal

    return dst


img = cv.imread('min_max.jpg', cv.IMREAD_GRAYSCALE)
minFiltered = minMaxFilterGray(img, 7, 0)
maxFiltered = minMaxFilterGray(img, 7, 1)

cv.imshow('img', img)
cv.imshow('min', minFiltered)
cv.imshow('max', maxFiltered)
cv.waitKey()