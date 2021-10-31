''' array manipulations '''

import numpy as np
array = np.arange(10,34,2)
print('original array: \n',array)
print('Reshaping the array : ')
print(array.reshape(3,4))
print('Flat array: ')
print(array.flatten())      #returns a copy of the array collapsed into one dimension
print('Ravel array: ')
print(array.ravel())        #returns a contiguous flattened array
print('Swap axes of the array:  ')
array = array.reshape(3,4)
print(np.swapaxes(array,1,0))       #to interchange two axes of an array. Here the row is interchanged with columns
print()
print('Rolls the specific axis backwards: ')
print(np.rollaxis(array,0))
print('To expand the dimension of the array : ')
print('Original array shape:  ',np.shape(array))
print('Expanded shape of the array:  ',np.expand_dims(array,axis=0))
print('Expanded shape of the array:  ',np.shape(np.expand_dims(array,axis=0)))
