# Create an image with blue, grean, red horizontal pattern
import cv2 as cv
import numpy as np

h = 480
w = 640
img = np.zeros((h, w, 3), dtype=np.uint8)

img[0:h//3, :] = (255, 0, 0)    # (B, G, R)
img[h//3: h//3*2, :] = (0, 255, 0)
img[h//3*2:, : ] = (0, 0, 255)

cv.imshow('img', img)
cv.waitKey()