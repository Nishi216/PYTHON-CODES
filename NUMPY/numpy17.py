''' arithmatic operations in numpy '''

import numpy as np
a = np.array([10,20,30,40,50,60])
b = np.arange(1,7,1)
print('Original arrays are:  \n',a,'\n',b)
print('two arrays are added :')
print(np.add(a,b))
print('two arrays are subtracted :')
print(np.subtract(a,b))
print('two arrays are multiplied :')
print(np.multiply(a,b))
print('two arrays are divided :')
print(np.divide(a,b))
print('reciprocal of the integers in array:  ')
print(np.reciprocal(a))
print('reciprocal of the decimals in array:  ')
print(np.reciprocal([0.25,1.33,3.14,0.60]))
print('Power of the numbers in the array:  ')
print(np.power(a,2))
print('power of the integers of an array using another array integer: ')
print(np.power(a,b))
print('To get the remainder: ')
print(np.mod(a,b))
print(np.remainder(a,b))

#to get the complex number operations in numpy
print()
com_array = np.array([5+0.6j,0.40j,11.,4.11j])
print('Array is: \n',com_array)
print('real part of the array is: \n',np.real(com_array))
print('imaginary part of the array is: \n',np.imag(com_array))
print('conjugate function: \n',np.conj(com_array))
print('getting the angle of the complex number in radian: \n',np.angle(com_array))
print('getting the angle of the complex number in degree: \n',np.angle(com_array,deg=True))
