string = "In 2020, the avg temperatures in bangalore were variying from 15-25.30. The humidity also increased from 50.5% to 70.24%."
import re
pat=re.findall('\d+\W*\d*', string
               )
print(pat)
str = "d 10.116.1.216 sfd 2.2.2.3 sdfsdf"
pat1= re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', str)
pat = re.compile(r"\s((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9]))")

match = re.findall(pat, str)

print(match)

import copy
from copy import deepcopy

l3= [[1,2],[3,4], 5]
l4= copy.copy(l3)
l5= copy.deepcopy(l3)
print(l4)
print(l5)

def remove_char(str, n):
    first_part = str[:n]
    last_part = str[n + 1:]
    return first_part + last_part

print(remove_char("yogesh", 3))

input = "a$b#c"
rever = [i for i in input if  i.isalnum()][::-1]
for i, j in enumerate(input):
    if not j.isalnum():
        rever.insert(i,j)
print("".join(rever))

mystr = "I love my India"
# print(mystr[::-1])
string=""
for i in mystr.split():
    string += i[::-1] + " "
    # print(string)
print(string)
print(" ".join([i[::-1] for i in mystr.split()]))
