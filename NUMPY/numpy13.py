''' Joining arrays , splitting arrays, adding or removing elements from array '''

import numpy as np
array1 = np.array([[10,20],[30,40]])
array2 = np.array([[1,2],[3,4]])
print('array concatenation : ')
result = np.concatenate((array1,array2),axis=0)
print('along the column: \n',result)
result = np.concatenate((array1,array2),axis=1)
print('along the rows: \n',result)
print()
print()

print('To join sequence of arrays along a new axis')
print('dimension of original array: ',np.ndim(array1))
result = np.stack((array1,array2))      #this increases the dimension
print('along the columns:\n',result)
print('dimension of resultant array:  ',np.ndim(result))
print()
print()

print('stacking the arrays column-wise')
result = np.hstack((array1,array2))
print(result)
print()
print()

print('stacking the arrays row-wise')
result = np.vstack((array1,array2))
print(result)
print()
print()

print('Splitting of the array into sub ararys ')
print('original array is:  \n',array1)
result = np.split(array1,2,1)
print('splitted array:  \n')
print(result)
print('Horizontal split of the array:')
result = np.hsplit(array1,2)
print(result)
print('Vertical split of the array: ')
result = np.vsplit(array1,2)
print(result)
print()
print()


print('appending a value to the end of an array:  ')
result = np.append(array2,[5,6,7,8])        #this will return a flattened array with the added  elements
print(result)
print('to insert a value in the array along the given axis before the given indices')
result = np.insert(array2,2,[5,6,7,8])      #syntax is np.insert(array1,index,elements to insert)
print(result)
print('to return a new array with sub arrays along an axis deleted: ')
array = np.arange(12).reshape(3,4)
print('Original array is:  \n',array)
result = np.delete(array,[3,7,11])  #syntax is np.delete(array, list of elements in the array to be deleted
print(result)
print('to find the unique elements in the array')
array = np.array([[10,10,2],[20,4,20],[20,10,10]])
print(np.unique(array))     #it will give unique values from the array
print('to resize the array')
print('original array is: \n',result)
print('resized array is: \n',np.resize(result,(3,3)))


