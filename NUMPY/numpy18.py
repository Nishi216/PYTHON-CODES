''' statistical functions  '''
import numpy as np
a = np.array([[10,20,30],[50,40,80],[70,20,60]])
print('The array is:  \n',a)
print('np.amin(a) : \n',np.amin(a))
print('np.amin(a,0) : \n',np.amin(a,0))
print('np.amin(a,1) : \n',np.amin(a,1))
print('np.amax(a) : \n',np.amax(a))
print('np.amax(a,0) : \n',np.amax(a,0))
print('np.amax(a,1) : \n',np.amax(a,1))
print('np.ptp(a) : \n',np.ptp(a))
print('np.ptp(a,0) : \n',np.ptp(a,0))
print('np.ptp(a,1) : \n',np.ptp(a,1))
print()
print('np.median(a) : \n',np.median(a))
print('np.median(a,0) : \n',np.median(a,0))
print('np.median(a,1) : \n',np.median(a,1))
print('np.mean(a) : \n',np.mean(a))
print('np.mean(a,0) : \n',np.mean(a,0))
print('np.mean(a,1) : \n',np.mean(a,1))
print()
print()

#now getting the weighted average - there is an arraya nd the corresponding weights and the
#weighted average is calculated by adding the product of the corresponding elements of the two arrays
#and dividing the sum by the sum of weights

array = np.array([1,2,3,4])
wts = np.array([4,3,2,1])
print('The array is:  \n',array)
print('After applying the weights:  \n')
print(np.average(array,weights=wts))
print(np.average(array,weights=wts,returned=True))  #returns the sum of the weights if returned is true

#calculating the standard deviation
#std = sqrt(mean(abs(x-x.mean())**2))
print('np.std(array) : \n',np.std(array))

#calculating the variance - mean(abs(x-x.mean())**2)
print('np.var(array) : \n',np.var(array))

