import re
p=re.compile('[a-e]')
string="hey, this is a test value"
print(p.findall(string))
print("\n")

string="hey, its 8pm of 11 june in 2021"
p=re.compile('[0-9]')
print(p.findall(string))
print("\n")

string="hey, its 8pm of 11 june in 2021"
p=re.compile('\d+')
print(p.findall(string))
print("\n")

string="hey, its 8pm of 11 june in 2021"
p=re.compile('\w+')
print(p.findall(string))
print("\n")

string="hey, its - 8pm of 11 june in 2021 ;"
p=re.compile('\W')
print(p.findall(string))
print("\n")

string="ababbaaabbbbab"
p=re.compile('ab*')
print(p.findall(string))
print("\n")

string="hey, its - 8pm of 11 june in 2021 ;"
p=re.split('\W',string)
print(p)
print("\n")

string="hey, its - 8pm of 11 june in 2021 ;"
p=re.split('\d',string)
print(p)
print("\n")