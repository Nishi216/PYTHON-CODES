''' Performing basic array operations on numpy array '''

import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[10,20],[30,40]])
print("Initial arrays are: ")
print("a = ",a)
print("b = ",b)
print()

print("Adding 10 with every elements of array a : ")
print(a+10)

print("Subtracting 10 from every element of array b : ")
print(b-10)

print("Multiplying 2 with every element of array a : ")
print(a*2)

print("Squaring every element of array a : ")
print(a**2)

print("Sum of all the elements of the array a : ")
print(a.sum())

print("Adding two arrays of a and b : ")
print(a+b)

print("Multiplying the arrays element-wise : ")
print(a*b)

print("Matrix multiplication of the arrays : ")
print(a.dot(b))

print("Getting the transpose of array b : ")
print("Original array : \n",b)
print("Transposed array : \n",b.transpose())
print()
print()

#Performing Unary operations
array = np.arange(1,10,1)
values = array.reshape(3,3)
print("The array is : \n", values)
print("The largest element in the array : ",values.max())
print("The largest element row-wise in array : \n",values.max(axis=1))
print("The largest element column-eise in array : \n",values.max(axis=0))
print("The smallest element in the array : ",values.min())
print("The cumulative sum along each row : \n",values.cumsum(axis=1))
print("The cumulative sum along each column : \n",values.cumsum(axis=0))
print()
print()

#Universal functions in numpy
new_array = np.array([0,np.pi/2,np.pi])
print("The original array is : ")
print(new_array)

print("Sine value of the array : \n",np.sin(new_array))
print("Cosine value of the array : \n",np.cos(new_array))
print("Exponentiation of the array : \n",np.exp(new_array))
print("Square root of the array : \n",np.sqrt(new_array))


























