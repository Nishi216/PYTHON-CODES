''' binary operations in arrays '''
import  numpy as np
array1 = np.array([[10,15],[5,10]])
array2 = np.array([[12,10],[8,12]])

print('Bitwise and operation is:  \n',np.bitwise_and(array1,array2))
print('Bitwise and operation:  \n',array1&array2)

print('Bitwise or operation is:  \n',np.bitwise_or(array1,array2))
print('Bitwise or operation:  \n',array1|array2)

print('Bitwise not operation is:  \n',np.invert(array1))
print('Bitwise not operation:  \n',~array1)

print('left shift operation is:  \n',np.left_shift(array1,3))
print('left shift operation:  \n',array1<<3)

print('right shift operation is:  \n',np.right_shift(array1,3))
print('right shift operation:  \n',array1>>3)