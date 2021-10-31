#to count all the duplicates from a string

no_of_chars=256  #specifying the total characters

def fillchar(string,count):
    for i in string:
        count[ord(i)]+=1
    return count

def printdup(string):
    count=[0]*no_of_chars
    count = fillchar(string,count)
    k=0
    for i in count:
        if int(i)>1:
            print( chr(k) + ", count = "+ str(i))
        k+=1

string="malayalam"
print(printdup(string))

print("\n\n")
#this method is bad in terms of space complexity as the character array of count is taking up a huge space each time

#method 2

from collections import defaultdict
def printdup(st):
    count=defaultdict(int)
    for i in range(len(st)):
        count[st[i]]+=1

    for it in count:
        if(count[it]>1):
            print(it, ", count = ", count[it])

st="malayalam"
printdup(st)

#time complexity for this is o(n log n) , where n= length of the string passed
#space complexity is o(k) , where k=size of map