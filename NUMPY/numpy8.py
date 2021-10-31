''' Numpy sorting '''

#Different ways of sorting
import numpy as np
array = np.array([[10,2,4],[5,9,1],[3,2,8]])
print('The array is : \n',array)
print('The sorted array is : \n',np.sort(array,axis=None))
print('Sorting array along the rows : \n',np.sort(array,axis=1))
print('Sorting array along the columns : \n',np.sort(array,axis=0))
print('Sorting array along the last axis: \n',np.sort(array,axis=-1))
print()
print()


array1 = np.array([9,3,4,2,8,7,1,6,9])
print('The array is : \n',array1)
indexes = np.argsort(array1)   #this will sort the array and then will provide the indexes for the sorted array
sorted_array = np.zeros(len(indexes),dtype=int)
for ele in range(len(indexes)):
    sorted_array[ele]=array1[indexes[ele]]
print("Sorted array is : ",sorted_array)
print()

array1 = np.array([9,3,4,2,8,7,1,6,9])
print('The array is : \n',array1)
array2 = np.array([5,4,9,2,3,7,0,9,8])
print('The array is : \n',array2)
for (i,j) in zip(array1,array2):
    print(i,' ',j)
result = np.lexsort((array2,array1))
print('Sorted indexes are : ',result)









