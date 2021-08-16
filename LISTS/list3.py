listed = [10,60,40,20,60,40]
first=['one','two','three','four','five','six']

#using insert(index,object)method - to insert an element at specific index
listed.insert(4,80)
print(listed)
first.insert(4,'seven')
print(first)
print()


#using extend(sequence) method - to append list to an existing list
seq=[1,2,3,4]
listed.extend(seq)
print(listed)
print()


#using count(element) - counts the number of appearance in the list
print('count of 40 is : ', listed.count(40))
print('count of three is : ', first.count('three'))
print()