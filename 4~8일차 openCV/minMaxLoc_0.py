import cv2 as cv
import numpy as np

img = np.array([[2, 1, 3],
                [7, 5, 4]], np.uint8)

minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(img)

print('img\n', img)
print('minVal = {}, minLoc = {}'.format(minVal, minLoc)) # 최소값과 최소값의 위치
print('maxVal = {}, maxLoc = {}'.format(maxVal, maxLoc)) # 최대값과 최대값의 위치

mask = np.array([[0, 1, 1],
                 [0, 1, 1]], np.uint8)

minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(img, mask=mask)

print('mask\n', mask)
print('minVal = {}, minLoc = {}'.format(minVal, minLoc))
print('maxVal = {}, maxLoc = {}'.format(maxVal, maxLoc))