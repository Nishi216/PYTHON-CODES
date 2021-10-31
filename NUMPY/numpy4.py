''' Sorting the numpy array in different ways '''

import numpy as np

array = np.array([[10,22,4],
                  [56,47,10],
                  [2,9,1]])
print("Original array is : \n",array)

#axis=None has to be specified for sorting the full array
print("Sorted array is : \n",np.sort(array, axis=None))

print("Sorting the array row-wise : \n",np.sort(array,axis=1))
print("Sorting the array column-wise : \n",np.sort(array,axis=0))
print()
print("Sorting the array column-wise by applying merge-sort")
print(np.sort(array,axis=0,kind='mergesort'))
print()


print("CREATING THE DATA TYPES AND THEN SORTING THE ARRAY")
data_types = [('name','S10'),('grad_year',int),('cgpa',float)]
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7),
           ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]
arr = np.array(values,dtype=data_types)
print("Original array is: ")
print(arr)
print("Array sorted by names : ")
print(np.sort(arr, order='name'))
print("Array sorted by graduation year and then cgpa")
print(np.sort(arr,order=['grad_year','cgpa']))








