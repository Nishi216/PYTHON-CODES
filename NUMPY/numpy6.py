''' Bitwise and binary operations in numpy '''

import numpy as np

array1 = np.arange(2,10,2)
array2 = np.linspace(10,18,4, dtype='int32')
print("First array : ",array1)
print("Second array : ",array2)
result = np.bitwise_and(array1,array2)
print("Bitwise AND operation on each elements is : \n",result)
print()
result = np.bitwise_or(array1,array2)
print("Bitwise OR operation on each elements is : \n",result)
print()
result = np.bitwise_xor(array1,array2)
print("Bitwise XOR operation on each elements is : \n",result)
print()
print("Original array is : \n",array1)
result = np.invert(array1)
print("Invertion of the array is : \n",result)
print()

print("Original array is : \n",array1)
result = np.left_shift(array1,2)
print("The left shifting of the array elements by 2 bits : \n",result)
print()

print("Original array is : \n",array2)
result = np.right_shift(array2,2)
print("The right shifting of the array elements by 2 bits : \n",result)
print()
print()

print("Binary representation of the array elements :  ")
numbers = np.array([2,6,-10,-8])
result = np.binary_repr(numbers[1])
print("The binary representation without using width : ",result)
result = np.binary_repr(numbers[1],width=6)
print("The binary representation using width : ",result)
result = np.binary_repr(numbers[2])
print("The binary representation of negative value without using width : ",result)
result = np.binary_repr(numbers[2],width=5)
print("The binary representation of negative value using width : ",result)


