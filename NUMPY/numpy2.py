'''Different ways of accessing elements in an array in numpy'''

import numpy as np
arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])
print('Initial array is:  ')
print(arr)
sliced_array = arr[:2,::2]
print("Taking first two rows and alternate columns : ")
print(sliced_array)

indexed_arr = arr[[0,0,1,2],[0,2,2,1]]
print("Array got by indexing :  ")
print(indexed_arr)
print()

print("Original array is : \n",arr)
array_indexing = arr[np.array([[1,2,0],[0,2,1]])]
print("Array got by using array as an index : \n",array_indexing)


print("Getting the elements of an array for which condition is true : ")
boolean_array = arr[arr%2==0]
print(boolean_array)


