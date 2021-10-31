#this is to match the date or get the date from the input string

import re
st= "I was born on September 16"
regex = r"([a-zA-Z]+) (\d+)"
match = re.search(regex, st)
if match != None:
    print("found at %s and ends at %s"%(match.start(),match.end()))
    print("date is: "+match.group(0))
    print("month is: "+match.group(1))
    print("date is: "+match.group(2))
else:
    print("no match found")


print("\n\n")
#use of teh match function

import re
def finddatemonth(st):
    regex = r"([a-zA-Z]+) (\d+)"
    mat = re.match(regex, st)
    if mat==None:
        print("not found")
        return
    print("date is: "+mat.group(0))
    print("month is: " + mat.group(1))
    print("day is: " + mat.group(2))
st= "I was born on September 16"
finddatemonth(st)
st="September 16"
finddatemonth(st)