#dict.fromkeys() - The fromkeys() method creates a new dictionary from the given sequence of elements with a value provided
# by the user. If the value argument is set, each element of the newly created dictionary is set to the provided value.
#this is basically creating a new dictionary with the provided keys (in the form of sequence ex. list) and the value is set to default single value

dict={}         #declaring an empty dictionary
seq=['one','two','three','four']      #initializing squence to be used as key
val=0       #setting the default value to 0 for each key

print('creating dictionary without any value:  ')
dict = dict.fromkeys(seq)
print(dict)
print()

print('creating dictionary with the default values')
dict = dict.fromkeys(seq,val)
print(dict)
print()
print()



