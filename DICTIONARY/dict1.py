#for creating a dictionary
dict = {'prog_lang1':'python','prog_lang2':'java','prog_lang3':'c++','prog_lang4':'javascript'}
print('The dictionary created is:  ')
print(dict)
print()


#to get only the keys from dictionary
print('The keys are:  ',dict.keys())         #this will give in list form
for val in dict.keys():           #this is for accessing individually
    print(val,end='     ')
print()
print()

#to get only the values from dictionary
print('The values are:  ',dict.values())         #this will give in list form
for val in dict.values():           #this is for accessing individually
    print(val,end='     ')
print()
print()


#for updating an existing dictionary - to update an old value or to add a new value
print('old dictionary: ',dict)
dict['prog_lang5']='PHP'
dict['prog_lang6']='HTML'
print('updated dictionary is: ',dict)
print()
print()


#to change the value of any existing key
dict['prog_lang5']='CSS'
print('New update:  ')
print(dict)

print()
#dict.items() - returns the key-value pairs in the form of tuples inside the list
print('The key value pairs are:  ')
print(dict.items())
print()
print('For getting access to key value pair tuples individually:  ')
for val in dict.items():
    print(val)
print()
print('For getting the keys and values separately:  ')
for key,value in dict.items():
    print('Key is :',key,end='    ')
    print('Value is:',value)




'''
SO HERE THE DICTIONARY METHODS USED ARE -
.keys()
.values()
.items()'''