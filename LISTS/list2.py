
#to convert a given tuple into list
tup=(10,20,30,40)
var=list(tup)
print(var)
print()

#to convert a given dictionary into list
number_pairs = {1:'one',2:'two',3:'three'}
x,y = list(number_pairs), list(number_pairs.values())
print('list of keys are: ', x)
print('list of values are:', y)
print()


#using .append() method
fruits=['apple','mango','grapes']
print(fruits)
fruits.append('banana')
print('after appending: ', fruits)