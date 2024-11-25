s = "yogeshyogkumar"

import re

r = re.split(s, 'y')  # will print [y]
print(r)

r = re.split('yog', s)  # will print ['', 'esh', 'kumar']
print(r)

# sub

r = re.sub('yog', 'k', s)
print(r)


#subn

r = re.subn('y', 'k', s)
print(r)

name = "Yogesh"

print ("my name is {0}".format(name))
print (f"my name is {name}")

import subprocess
user = 'ape'
host = '10.204.90.31'
# process = subprocess.Popen("ssh {user}@{host} {cmd}".format(user=user, host=host, cmd='ls -l'),
#                            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
strs= "yogeshkumardewangan"
j={}
for i in strs:
    if i in j:
        j[i] += 1
    else:
        j[i] =1
print(j)
my_array = [1,1,2,2,2,3,5,3,3,1,3,3,3,3,4,4,5,5,5,5,5,5,5,5,5,5]
a=max({key: my_array.count(key) for key in my_array})
print(my_array.count(a))
# def find_element_occurances_using_dict(array):
#     dict={}
#     for char in array:
#         if char in dict.keys():
#             dict[char]=dict[char]+1
#         else:
#             dict[char]=1
#
#     print(dict)
#     max_key = max(dict, key=dict.get)
#     print(max_key)
#     print(dict[max_key])
#
# find_element_occurances_using_dict(my_array)

dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(max(dict.keys()))
for key, value in dict.items():
    print(key+ ": "+ str(value) )


print(dict[max(dict)])
print(dict[min(dict)])

def fib(n):
    p,q = 0,1
    while p < n:
        yield p
        p,q = q, p+q
n=10
x=fib(n)
for i in x:
    print((i))

my_array = [2, 6, 1, 7, 9, 4, 1]
rm_dup = list(set(my_array))
if len(my_array) == len(rm_dup):
    print("No dups")
print([i for i in my_array if my_array.count(i)>1])

string="Hello from shu.bhamg199630@gmail.com to priya@yahoo.com about the meeting @2PM"
import re
print(re.findall('\S+@\S+', string))
print(re.findall('[0-9]+', string))

color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]
print(set(color1)&set(color2))
print([x for x in color1 if x in color2])

from random import shuffle
shuffle(color1)
print(color1)

list = [25,4,6,7,8,2,3,4,9]
list.sort()
print(list[0])
smallest = list[0]
for i in list:

    if i < smallest:
        smallest = i
print(smallest)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [9, 8, 7, 6, 5, 4, 3, 2]
odd_first = [i for i in list1 if i%2 ==0] + [i for i in list2 if i%2 !=0]
print(odd_first)
print("First List - " + str(list1[1::2]))
print("Second List - " + str(list2[0::2]))
list3 =[]
list3.extend(list1[1::2])
list3.extend(list2[0::2])
print("Final List - " + str(list3))

for i in range(2000,3001):
    if i % 7 ==0 and i%5 !=0:
        print(i, end=", ")

#palindrome
st = "112233445566778899000000998877665544332211"
print(st)
print(st[::-1])
if st == st[::-1]:
    print("yes")

a='Geeksforgeeks'
b=''
for i in a:
    b= i+b
print(b)

##permut
from  itertools import permutations

ini_str = "abc"
data = permutations(ini_str)
for i in data:
    print(''.join(i))
# # Printing initial string
# print("Initial string", ini_str)
#
# # Finding all permutation
# result = []
#
#
# def permute(data, i, length):
#     if i == length:
#         result.append(''.join(data))
#     else:
#         for j in range(i, length):
#             # swap
#             data[i], data[j] = data[j], data[i]
#             permute(data, i + 1, length)
#             data[i], data[j] = data[j], data[i]
#
#
# permute(list(ini_str), 0, len(ini_str))

# Printing result
# print("Resultant permutations", str(result))

list = [3, 2, 5, 1, 8, 7]

rotation =2
for i in range(rotation):
    temp = list[0]
    for j in range(len(list)):
        if j+1 == len(list):
            list[j] = temp
            break
        list[j]=list[j+1]


print(list)