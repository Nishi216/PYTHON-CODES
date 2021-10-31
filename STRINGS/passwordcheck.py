#code to check the validity of the password
#method 1
import re
password=input("enter your password: ")
flag=0
while(True):
    if len(password)<8:
        flag=-1
        print("password should have at least 8 characters")
        break
    elif not re.search("[a-z]",password):
        flag=-1
        print("atleast one value from a-z should be there")
        break
    elif not re.search("[A-Z]",password):
        flag=-1
        print("atleast one value from A-Z should be there")
        break
    elif not re.search("[0-9]",password):
        flag=-1
        print("atleast one value from 0-9 should be there")
        break
    elif not re.search("[_@#$]",password):
        flag=-1
        print("atleast one value in _ @ # $ should be there")
        break
    elif re.search('\s',password):     #if any white space is found
        flag=-1
        print("tehre should be no white space")
        break
    else:
        flag=0
        print('valid password :)')
        break
if flag==-1:
    print("enter password again :(")


#method 2
l,u,d,p=0,0,0,0
password=input("enter your password: ")
if(len(password))>8:
    for i in password:
        if i.islower():
            l+=1
        if i.isupper():
            u+=1
        if i.isdigit():
            d+=1
        if (i=='@' or i=='#' or i=='$' or i=='_'):
            p+=1
if (l>=1 and u>=1 and d>=1 and p>=1 and l+u+d+p==len(password)):
    print("valid password :)")
else:
    print("invalid password :(")
