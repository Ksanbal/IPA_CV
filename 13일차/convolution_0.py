import numpy as np

mat0 = np.array([[0,1,0], [1,2,1], [0,1,0]])
mat1 = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(mat0)
print(mat1)

sum = 0
for i in range(3):
    for j in range(3):
        sum += mat0[i,j] * mat1[i,j]

print('sum : ', sum)

mat_mul = mat0 * mat1
print('mat_mul\n', mat_mul)
mat_mul = np.multiply(mat0, mat1)
print('np)mat_mul\n', mat_mul)
print('np)mat_mul.sum\n', mat_mul.sum())