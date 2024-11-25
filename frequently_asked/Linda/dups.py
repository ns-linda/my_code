my_array = [2, 6, 1, 7, 9, 4, 1]
my_array.sort()
for i in range(len(my_array)-1):
    if my_array[i] == my_array[i+1]:
        print("yes")

import re
string="Hello from shu.bhamg199630@gmail.com to priya@yahoo.com about the meeting @2PM"

match = re.findall('\S+@\S+', string)
print(match)

match_d = re.findall('[0-9]+',string)
print(match_d)

def fac(n):
    if n<=1:
        return 1
    else:
        print(n, n-1)
        return n*fac(n-1)
print(fac(4))
n=4
fac=1
for i in range(1,n+1):
    fac = fac*i
print(fac)

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(9))

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)
from random import shuffle
shuffle(color)
print(color)

from math import fsum





from math import fsum


array=[2,1,3,6,4,7,8]


def find_missing_number(array):
    n= len(array)
    total = (n+1)*(n+2)/2
    sum = int(fsum(array))
    return int(total-sum)


print (find_missing_number(array))

def first_non_repeated_element(array):
    for i in range(len(array)):
        count=0
        for j in range(len(array)):
            if array[i]==array[j]:
                count+=1


        if count<=1:
            return array[i]


my_array= "aabbccdef"
print(first_non_repeated_element(my_array))
s="9"
for i in range(len(my_array)):
    s=my_array[i]
    print(s)
    for j in range(i+1):
        print(my_array[j])

