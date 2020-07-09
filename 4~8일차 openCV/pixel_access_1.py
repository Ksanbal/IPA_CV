import cv2 as cv
import numpy as np

s = 500
img = np.zeros((s, s), dtype=np.uint8)

for i in range(s):
    for t in range(s):
        # 0 <= i+t <= 499+499(s-1+s-1)
        # i+t = 0       -> 밝기 = 0
        # i+t = 499+499 -> 밝기  = 255
        img[i, t] = (i+t) * 255//(2*s-2)

cv.imshow('img', img)
cv.waitKey()