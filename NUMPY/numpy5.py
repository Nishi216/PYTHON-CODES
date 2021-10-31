''' using the numpy array iterator to iterate over the elements'''

import numpy as np
array = np.arange(12)
array = array.reshape(3,4)

print("Original Array is : \n",array)
print("Modified array is : ")
for ele in np.nditer(array):
    print(ele)

trans_array = array.T
print("Transposed array iteration is  : ")
for ele in np.nditer(trans_array):
    print(ele)


print("Modified array in C style order : ")
for ele in np.nditer(array, order = 'C'):
    print(ele, end=' ')

print()
print("Modified array in F style order : ")
for ele in np.nditer(array, order = 'F'):
    print(ele, end=' ')

print()
print("Modifying the array values : ")
print("Original array : \n",array)
for ele in np.nditer(array,op_flags=['readwrite']):
    ele[...]=10*ele
print("Modified array is : \n",array)

print()
print("Broadcasting arrays : ")
array1 = np.array([[1,2,3,4],[5,6,7,8],[2,4,6,8]])
print("First array : \n",array1)
array2 = np.array([10,20,30,40])
print("Second array : \n",array2)
print("Modified array is : ")
for x,y in np.nditer([array1,array2]):
    print('%d : %d'%(x,y))
