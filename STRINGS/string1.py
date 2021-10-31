# DIFFERENT FORMAT SPECIFIERS FOR STRINGS

string1="{} {} {}".format('python','is','fun');
print(string1)
string2="{2} {1} {0}".format('python','is','fun');
print(string2)
string3="{b} {c} {a}".format(b='python',c='is',a='fun');
print(string3)


name="|{:<10} |{:^10} |{:>10}|".format('python','is','good')
print(name)

def fun():
    '''this is just for demonstration
    of the use of docstring type in python'''
    return None

print("printing the documentation of the function: ")
print(fun.__doc__)