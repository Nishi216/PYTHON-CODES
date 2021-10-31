#for converting a string into list
#method 1
def convert(string):
    li=list(string)
    return li

string="python is good"
print(convert(string))

print("\n")
#method 2
def convert(string):
    li=list(string.split(" "))
    return li

string="python is good"
print(convert(string))
print("\n")

#code to count and display the number of vowels
#method 1
def checkvowel(string,vowels):
    final=[i for i in string if i in vowels]
    print(len(final))
    print(final)
string="hello world, we are learning python"
vowels="aeiouAEIOU"
checkvowel(string,vowels)
print("\n")


#method 2 - by using dictionary
def checkvowel(string,vowels):
    string=string.casefold()       #casefold() is used to ignore the cases of string
    dic={}
    sum=0
    count=dic.fromkeys(vowels,0)
    for i in string:
        if i in count:
            count[i]+=1
    for i in (count.values()):
        sum+=i
    print("total number of vowels: ",sum)
    return count

string="hello world, we are learning python"
vowels='aeiou'
print(checkvowel(string,vowels))
print("\n")

#program to find the substring in a given string
#method 1
def findstr(string, substr):
    if string.find(substr)==-1:
        print("no")
    else:
        print("yes")
        print("substring found at: ",string.find(substr))
string="python is fun"
substr="id"
findstr(string,substr)
print("\n")

#method 2 - by using count()
def findstr(string,substr):
    if string.count(substr)>0:
        print("yes")
        print("substring at: ",string.find(substr))
    else:
        print("no")
string="python is fun"
substr="is"
findstr(string,substr)
print("\n")

#program to check if two strings are anagram
#method 1 - using the sorted()
def checkana(string1,string2):
    if sorted(string1)==sorted(string2):
        print("{} and {} are anagrams".format(string1,string2))
    else:
        print("%s and %s are not anagrams"%(string1,string2))
string1="listen"
string2="silent"
checkana(string1,string2)

#method 2 - using counter
from collections import Counter
def checkana(string1,string2):
    if Counter(string1)==Counter(string2):
        print("{} and {} are anagrams".format(string1,string2))
        print(Counter(string1))
        print(Counter(string2))
    else:
        print("they are not anagrams")
string1="listen"
string2="silent"
checkana(string1,string2)