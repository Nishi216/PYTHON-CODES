''' creating array from existing data '''

import numpy as np
list1 = [3,4,5]
array1 = np.asarray(list1)
print('The array by asarray method is:  ',array1)
list2 = [(1,2,3),(4,5,6)]
array2 = np.asarray(list2)
print('The array using asarray method is : \n',array2)
print()

list3 = range(10)
it = iter(list3)
array3 = np.fromiter(it,dtype=float)
print("array created using fromiter :  ",array3)
print()
print()

# using nditer in different ways

array = np.arange(0,60,5)
array = array.reshape(3,4)
print('Original array is: \n',array)
print('Modified array is:  ')
for ele in np.nditer(array):
    print(ele,end=' ')
print()

array1 = array.copy(order='C')
array2 = array.copy(order='F')
print('Sorted in the C style order :  ')
for ele in np.nditer(array1):
    print(ele,end=' ')
print()
print('Sorted in the F style order :  ')
for ele in np.nditer(array2):       #for ele in np.nditer(array, order='F')
    print(ele,end=' ')
print()
print()

#using op_flags
print("Original array is:   \n",array)
for ele in np.nditer(array,op_flags=['readwrite']):   #will do inplace array modification
    ele[...]=2*ele
print('Modified array is:   \n',array)
print()
print()

#broadcasting iteration
array2 = np.array([1,2,3,4])
print("First array is: \n",array)
print("Second array is: \n",array2)
print("Broadcasted array is: ")
for x,y in np.nditer([array,array2]):
    print("%d:%d"%(x,y), end="    ")







