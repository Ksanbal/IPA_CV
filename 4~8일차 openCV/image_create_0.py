# 이미지를 직접 생성해보기
import cv2 as cv
import numpy as np

# np_img = np.zeros((480, 640), dtype=np.uint8)
np_img = np.full((480, 640), 120, dtype=np.uint8)
# img = cv.imwrite('test.jpg', np_img)

cv.imshow('img', np_img)
cv.waitKey()