#to check if teh string is a palindrome or not

#method 1

def isplaindrome(st):
    return st==st[::-1]

st="malayalam"
result=isplaindrome(st)
if result:
    print("yes")
else:
    print("no")


#method2

def ispalindrome(st):
    for i in range(0,int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
        return True
st="malayalam"
result=isplaindrome(st)
if result:
    print("yes")
else:
    print("no")

#method 3 - using recursion

def ispalindrome(st):
    st=st.lower()
    l=len(st)
    if l<2:
        return True
    elif st[0]==st[l-1]:
        return isplaindrome(st[1:l-1])
    else:
        return False

s="malayalam"
result=isplaindrome(s)
if result:
    print("yes")
else:
    print("no")