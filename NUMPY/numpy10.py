''' Creating your own data type and using it to create the array '''

import numpy as np
dt = np.dtype(np.int64)
print('The data type is: ',dt)
print()

dt = np.dtype([('age',np.int32)])
print('The data type defined is: ',dt)
print('The data type of age is: ',dt['age'])
print()

dt = np.dtype([('name','S20'),('age',np.int32),('cgpa','f4')])
student = np.array([('abc',18,8.65),('ngh',20,9.31),('kjh',19,9.00)],dtype=dt)
print('The data type corresponding to the names are:  ',dt)
print('The array is:  ',student)
print('Name of the students : ')
for names in student['name']:
    print(names)
