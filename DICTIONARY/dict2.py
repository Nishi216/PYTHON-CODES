#for deleting value/values from the dictionary - del keyword is used
dict = {'prog_lang1':'python','prog_lang2':'java','prog_lang3':'c++','prog_lang4':'javascript'}
print('Original dictionary is:  ')
print(dict)
del dict['prog_lang4']           #value is accessed by the key
print()
print('After deletion, the dictionary is: ')
print(dict)
print()


print('Now to clear all the key value pairs')
dict.clear()        #to delete all elements
print('all the values have got cleared: ',dict)
print()


print('Now delete the dictionary')
del dict  #this deletes the dictionary as a whole
print()
print()


'''
SO HERE THE DICTIONARY METHODS USED ARE -
.clear()
THE KEYWORD FOR DELETION IS
del name_of_dictionary'''