# numpy와 openCV의 산술연산

import cv2 as cv
import numpy as np

mat0 = np.uint8([[130,140], [150, 160]])
mat1 = np.uint8([[100,100], [100, 100]])
mat2 = np.uint8([[145,145], [145, 145]])

print('mat0')
print(mat0)
print('mat1')
print(mat1)
print('mat2')
print(mat2)

print('mat0 + mat1')
print(mat0 + mat1)              # 255를 넘으면 overflow 발생

print('cv.add(mat0, mat1)')
print(cv.add(mat0, mat1))       # 255를 max로 두고 overflow 방지

print('mat0 - mat2')
print(mat0 - mat2)              # 0 이하로 내려가면 underflow 발생

print('cv.subtract(mat0, mat2)')
print(cv.subtract(mat0, mat2))  # 0을 min으로 두고 underflow 방지

print('cv.addWeighted')
print(cv.addWeighted(mat0, 0.7, mat1, 0.3, 0))  # (src1, alpha, src2, beta, gamma)
# src1 * alpha + src2 * beta + gamma
# aplha와 beta의 합은 1이 되어야한다.
