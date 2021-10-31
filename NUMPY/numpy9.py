''' Different ways of searching in numpy and counting in numpy '''

import numpy as np
array = np.array([[10,16,2],[7,18,5],[12,4,9]])
print("The array is : \n",array)
print('Maximum element in the array : ',array.max())
print('Index of maximum element in the array : ',np.argmax(array))
print('Index of max element row-wise : ',np.argmax(array,axis=1))
print('Index of max element column-wise : ',np.argmax(array,axis=0))
print()

print('Minimum element in the array : ',array.min())
print('Index of minimum element in the array : ',np.argmin(array))
print('Index of minimum element row-wise : ',np.argmin(array,axis=1))

array1 = np.array([[0,1,7,0,0],[3,0,0,2,19]])
a = np.count_nonzero(array1)
b = np.count_nonzero(array1, axis=0)
print("Number of nonzero values is :", a)
print("Number of nonzero values along columns is :", b)