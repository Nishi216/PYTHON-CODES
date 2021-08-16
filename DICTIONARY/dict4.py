#str(dict) - gives the string representation of the dictionary
dict= {'prog_lang1':'python','prog_lang2':'java','prog_lang3':'c++','prog_lang4':'javascript'}
print(dict)
print(str(dict))
print()
print()

#using .copy() - this is for shallow copy of the dictionary
dict={'prog_lang1':'python','prog_lang2':'java','prog_lang3':'c++','prog_lang4':'javascript'}
dict2=dict.copy()
print(dict)
print(dict2)
print()
print()
print('changing second dictionary won\'t change the first due to shallow copy: ')
dict2['prog_lang4']='HTML'
print(dict)
print(dict2)
print()
print()
print('changing first dictionary won\'t change the second due to shallow copy: ')
dict['prog_lang2']='Ruby'
print(dict)
print(dict2)


'''
SO HERE THE DICTIONARY METHODS USED ARE -
.copy()
THE FUNCTION USED IS - str()'''