#reversing a string
#method 1

def reversing(st):
    string="".join(reversed(st))
    return string

st="hello world!"
print("original string is: ",st)
print("the reversed string is: ",reversing(st))



#method 2
def reversing(st):
    str=""
    for i in st:
        str=i+str
    return str
st="hello world!"
print("original string is: ",st)
print("the reversed string is: ",reversing(st))



#method 3 - using recursion
def reversing(st):
    if len(st)==0:
        return st
    else:
        return reversing(s[1:]) + s[0]
st="hello world!"
print("original string is: ",st)
print("the reversed string is: ",reversing(st))