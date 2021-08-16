
#dict.update(dict2) - this is going to update the old dictionary adding the values from new dictionary. Dictionary to be added is placed inside the parenthesis
dict={'prog_lang1':'python','prog_lang2':'java','prog_lang3':'c++','prog_lang4':'javascript'}
dict2= {'prog_lang5':'HTML','prog_lang':'CSS'}
print('DICTIONARY BEFORE UPDATE:  ')
print(dict)
dict.update(dict2)
print('DICTIONARY AFTER UPDATE:  ')
print(dict)
print()


#dict.get(key, default=None) - this is to get the value corresponding to the key; none otherwise
dict={'prog_lang1':'python','prog_lang2':'java','prog_lang3':'c++','prog_lang4':'javascript'}
print('Getting the value using .get() method')
val=dict.get('prog_lang1')      #same as dict['prog_lang1']
val2=dict.get('prog_lang5',None)
print(val)
print(val2)
print('The dictionary will remain unchanged')
print(dict)
print()

#using dict.setdefault(key, default=None) - similar to get, but will create a key with the default value if key isnt there
dict={'prog_lang1':'python','prog_lang2':'java','prog_lang3':'c++','prog_lang4':'javascript'}
print('Getting the value using .setdefault() method')
val=dict.setdefault('prog_lang1')
val2=dict.setdefault('prog_lang5','CSS')
print(val)
print(val2)
print('The dictionary will change and the new value will get added')
print(dict)
print()


'''
SO HERE THE DICTIONARY METHODS USED ARE -
.update()
.get()
.setdefault()'''