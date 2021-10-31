''' mathematical functions are '''
#Triginometric functions

import numpy as np
array1 = np.array([0,30,45,60,90])
print('Sine of the angles: ')
print(np.sin(np.pi/180*array1))
print('\n')
print('Cosine of the angles: ')
print(np.cos(np.pi/180*array1))
print('\n')
print('Tangent of the angles: ')
print(np.tan(np.pi/180*array1))
print('\n')

#arcsin, arccos, arctan returns the trigonometric inverse of the sin cos and tan
sin = np.sin(np.pi/180*array1)
inv = np.arcsin(sin)
print('sin angles are: ')
print(sin)
print('Inverse of the sin angles:  ')
print(inv)
print('Degree of sin :  ')
print(np.degrees(sin))
print('Degree of reverse of sin :  ')
print(np.degrees(inv))
# same goes for cos and tan

#rounding of numbers
print()
array = np.array([10.25,20.56,30.44,40.86])
print('Original array is:  ')
print(array)
print('After rounding of:  ')
print(np.around(array))
print(np.around(array,decimals=1))
print(np.around(array,decimals=-1))
print(np.floor(array))
print(np.ceil(array))