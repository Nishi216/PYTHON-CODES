#using len(list1) to calculate the length of list
first=['one','two','three','four','five','six']
second=[30,50,70,90]
var=len(first)
print(var)
var=len(second)    #at this point, var will point at the 'second' object
print(var)
print()
print()



#using max(list) to return the maximum value
var=max(first)
print('maximum in the first list is: ', var)
var=max(second)
print('maximum in the second list is: ',var)
third = [100,20,5,6]
var=max(second, third)          #it will return the list having the maximum value element (at least one max value)
print(var)
print()



#using min(list) to return the minimum value
var=min(first)
print('minimum in the first list is: ', var)
var=min(second)
print('minimum in the second list is: ',var)
var=min(third, second)
print(var)
print()