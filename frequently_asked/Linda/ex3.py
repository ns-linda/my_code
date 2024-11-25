x,y=10,30
big= x if x>y else y
print(big)

import re
s='beautifulful'
print(re.split('a', s))
print(re.sub('ful', 'fy', s))
print(re.subn('ful', 'fy', s))

t1 = ('a', 'b', 'c', 'd', 'e', 'f')
t2 = (1, 2, 3, 4)
print(zip(t1,t2))
a0=dict(zip(t1,t2))
A1 = range(10)
print("A1: " + str(A1))
#
# a2=[i for i in A1 if i in a0]
# print(a2)

import threading
class Mythread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self)
        self.threadname=threadname

    def run(self):
        print("The threadname is ", self.threadname)

obj= Mythread("my thread")
obj.start()

mystr= "I love my India"
print(mystr[::-1])
s=mystr.split()
print(" ".join([i[::-1] for i in s]))
input = "a$b#c"
reverse = [i for i in input if i.isalpha()][::-1]

for i, j in enumerate(input):
    if not j.isalpha():
        reverse.insert(i,j)
print("".join(reverse))

def remove_char(str, n):
    s=[i for i in str]
    print(s)
    s.pop(n)
    return "".join(s)

print(remove_char("yogesh", 3))

def last_2(str):
    return str[2:]+str[:2]
print(last_2("yogesh"))

mystr = "yogesh"
s= mystr[-1:2]
print (mystr[0:2] + mystr[-2:])

list1 = ["i", "love", "my", "india", "fsdfsdfsdssd"]
d={i:len(i) for i in list1}
print(max(d, key = lambda x: d[x]))

input = "aaabbacc"
d={}
for i in input:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

from copy import copy, deepcopy
l3= [[1,2],[3,4], 5]
l4=copy(l3)
l5=deepcopy(l3)
print(l4)
print(l5)
#find and validate ip
str = "d 10.116.1.216 sfd 2.2.2.3 sdfsdf"
pattern = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
pat=re.findall(pattern, str)
print(pat)
pattern1=re.compile(r'\s((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])')
find= re.findall(pattern1, str)
print(find)
string = "In 2020, the avg temperatures in bangalore were variying from 15-25.30. The humidity also increased from 50.5% to 70.24%."
pat= re.findall('\d+\.?\d*?', string)
print(pat)

# import xml.dom.minidom as xml
# parse = xml.parse("path")

with open("ex.txt" , "r") as txt:
    for line in txt:
        print(line)
    # while True:
    #     linebreak= txt.read(1024)
    #     print(linebreak)
import os
print(os.stat("ex.txt").st_size)

python_dict = {
    "username": "jiangnanmax",
    "age": 21
}
import json
print(json.loads("""{"name":"Linda"}"""))
print(json.load(open("1.json", "r")))
file= open("2.json", "w")
file1= open("3.json", "w")
json.dump(python_dict, file)
file1.write(json.dumps(python_dict))

import pickle
f=open("pickle.txt", "ab")
val=10
pickle.dump(val,f)

file=open("pickle.txt", "rb")
value=pickle.load(file)
print(value)

import mo
def func():
    print("This is not called")
obj = mo.Myclass()
obj.func()

my_array = [2, 6, 1, 7, 9, 4, 2]
dups=[(i,j) for i, j  in enumerate(my_array) if my_array.count(j)>1]
print(dups)

string="Hello from shu.bhamg199630@gmail.com to priya@yahoo.com about the meeting @2PM"
pat= re.findall('\S+@\S+', string)
print(pat)

def fac(n):
    if n<=1:
        return 1
    else:
        return n * fac(n-1)
print(fac(4))

def fib(n):
    if n ==0:
        return 0
    elif n<=2:
        return 1
    else:
        return fib(n-1)+ fib(n-2)
print(fib(9))

from random import shuffle
lst=[3,4,5,6,8,1,2]
(shuffle(lst))
print(lst)
array=[2,1,3,4,5,7,8]
suma= sum(array)
n=len(array)
total= (n+1)*(n+2)//2
sum = total-suma
print(sum)

def non_repeated(str):
    substring=''
    for i in range(len(str)):
        substring=str[i]
        for j in range(i,len(str)):
            if str[j] not in substring:
                substring = substring + str[j]
                print(substring)
non_repeated("aabbccdef")
a="aabbccdef"
nw={}
for i in a:
    if i not in nw:
        nw[i]=a.count(i)
print(nw)



lst1 ='abc'
a=[i for i in lst1]
from itertools import permutations
j=permutations(a)
print(list(j))

##permutations
result=[]
def perm(a,i,l):
    if i==l:
        result.append("".join(a))
    else:
        for j in range(i,l):
            a[i], a[j]=a[j],a[i]
            perm(a,i+1,l)
            a[i], a[j] = a[j], a[i]
    return result
ini='abc'
print(perm(list(ini),0, len(ini)))

