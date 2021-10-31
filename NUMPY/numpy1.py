''' Different ways of creating an array in numpy '''
import numpy as np

print("Creating 1D array from list : ")
arr1 = np.array([10,20,30])
print(arr1)

print()
print('Creating 2D array from list : ')
arr2 = np.array([[10,20,30],
                 [40,50,60]])
print(arr2)

print()
print('Creating 3D array from tuple : ')
arr3 = np.array(((1,2,3),(4,5,6),(7,8,9)))
print(arr3)

print()
print("Characteristics of an array (of arr3) : ")
print("Type of array : ",type(arr3))
print("Type of elements inside the array : ",arr3.dtype)
print("Dimension of array : ",arr3.ndim)
print("Shape of array (No of rows and columns) : ",arr3.shape)
print("Size of array (No of elements in it) : ",arr3.size)

print()
print("Other ways for creating an array : ")
print("Creating an array with all zeros :  ")
zero_array = np.zeros((2,2))
print(zero_array)
print()

print("Creating an array with all ones : ")
ones_array = np.ones((2,3))
print(ones_array)
print()

print("Creating an array with all random values : ")
random_array = np.random.random((2,2))
print(random_array)
print()

print("Creating an array with arange : ")
arange_array = np.arange(0,20,2)
print(arange_array)
print()

print("Creating an array with linspace : ")
linspace_array = np.linspace(0,20,10)
print(linspace_array)
print()

print("Creating a complex array : ")
complex_array = np.full((2,2),5,dtype='complex')
print(complex_array)
print()

print("Reshaping the array : ")
arr = np.array([[1, 2, 3, 4],
                [5, 2, 4, 2],
                [1, 2, 0, 1]])
newarr = arr.reshape(2, 2, 3)
print("Original array:\n", arr)
print("Reshaped array:\n", newarr)
print()

print("Flattened array : ")
flat = newarr.flatten()
print(flat)
print()

print("To return the size of each elements in the array: ")
print("The array is:  ",arr)
print("The elements in the array is of ",arr.itemsize," bytes each")








