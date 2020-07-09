# bgr -> rgb using slicing [start:stop:step]

import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('cat.jpg', cv.IMREAD_COLOR)[:, :, ::-1] # 3차원 배열이니까(세로, 가로, 컬러)

plt.imshow(img, interpolation='bicubic')
plt.xticks([])
plt.yticks([])
plt.show()