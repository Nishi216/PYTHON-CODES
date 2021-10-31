''' Linear algebra in numpy '''

import numpy as np

array = np.array([[6,1,1],[4,-2,5],[2,8,7]])
print("Rank of array : ",np.linalg.matrix_rank(array))
print('Trace of the matrix : ',np.trace(array))
print('Determinant of matrix : ',np.linalg.det(array))
print('Inverse of matrix : ',np.linalg.inv(array))
print('Matrix raised to the power of 2 : ',np.linalg.matrix_power(array,2))


#For more matrix and linear algebra opeartions - follow https://www.geeksforgeeks.org/numpy-linear-algebra/
