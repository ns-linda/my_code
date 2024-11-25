my_tuple = ('sara', 6, 5, 0.97)
my_list = ['sara', 6, 5, 0.97]
print(my_tuple[0])     # output => 'sara'
print(my_list[0])     # output => 'sara'
# my_tuple[0] = 'ansh'    # modifying tuple => throws an error
my_list[0] = 'ansh'    # modifying list => list modified
print(my_tuple[0])     # output => 'sara'
print(my_list[0])

class Student:
   def __init__(self, fname, lname, age, section):
       self.firstname = fname
       self.lastname = lname
       self.age = age
       self.section = section
# creating a new object
stu1 = Student("Sara", "Ansh", 22, "A2")

#pass, conitnue, break
pat = [1, 3, 2, 1, 2, 3, 1, 0, 1, 3]
current = 0
for p in pat:
    pass
    if p==0:
        current =p
        break
    elif p%2==0:
        continue
    print(p, end=",")
print(current)


##slicing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1::2])

##array and list
import array
ar_l = array.array('i',[1,2,4])
for i in ar_l:
    print(i)
a=[1,2,'string']
print([i for i in a ])

#global
temp = 10   # global-scope variable
def func():
     global  temp
     temp= 20   # local-scope variable
     print(temp)
print(temp)   # output => 10
func()    # output => 20
print(temp)

##decorator
def inner(func):
    def smartmul(a,b):
        a=a*a
        b=b*b
        return func(a,b)
    return smartmul

@inner
def add(a,b):
    return a+b

print("decorator",add(2,3))

def splitdeco(func):
    def wrapper():
        return func().split()
    return wrapper

def changecasedeco(func):
    def wrapper():
        return func().lower()
    return wrapper

@splitdeco
@changecasedeco
def hello():
    return "HELLO WORLD"

print(hello())

# decorator function to capitalize names
def capitalise(func):
    def wrapper(arg1, arg2):
        string1 = arg1.capitalize()
        string2= arg2.upper()
        return func(string1,string2)
    return wrapper

@capitalise
def send_names(name, course):
    return "My name is " + name + " and am doing course: " + course

print(send_names("linda", "pcmb"))

##list and dict
my_list = [2, 3, 5, 7, 11]
print([x**2 for x in my_list])
print({x : x**2 for x in my_list})

a = [1, 2, 3]
b = [7, 8, 9]
print([(x,y) for x in a for y in b])
print([x+y for x, y in zip(a,b)])

my_list = [[10,20,30],[40,50,60],[70,80,90]]
print([y for x in my_list for y in x])

### lambda
mul = lambda a,b: a*b
print(mul(2, 5))

def wrapper(b):
    return lambda a: a*b
mul=wrapper(5)
print(mul(2))

## copy and deep copy
from copy import copy, deepcopy
list_1 = [1, 2, [3, 5], 4]
list_2 = list_1.copy()
print(list_2)
list_2[0] = 0
print(list_2)
list_3= deepcopy(list_1)
print(list_1)
list_3[0]=1
print(list_1)

##pickling
import pickle
f=open("1.txt", "wb")
val = 1000
pickle.dump(val,f)

f=open("1.txt", "rb")
value=pickle.load(f)
print(value)

###generator
def fib(n):
    p,q = 0,1
    while p < n:
        yield p
        p,q = q, p+q

n=10
x=fib(n)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())

def appendnumber(arr):
    arr.append(4)
    return arr

arr=[1,2,3,4]
print(appendnumber(arr))

##iterators
class Arraylist:
    def __init__(self, arr):
        self.arr=arr

    def __iter__(self):
        self.pos = 0
        return self

    def __next__(self):
        if self.pos < len(self.arr):
            self.pos +=1
            return arr[self.pos-1]

obj = Arraylist([1,2,3])
it = iter(obj)
print(it.__next__())
print(it.__next__())
print(it.__next__())

##remove file
import os
# os.remove("2.json")
print("file removed")

##split and join function
string = "This is a string."
print(string.split() )
print("".join(string))

def multiply(a, b, *args):
    mul = a*b
    for num in args:
        mul *=num
    return mul

print(multiply(1, 2, 3, 4, 5)) #output: 120

def keyarg(**kwargs):
    for i, j in kwargs.items():
        print(i +":"+j)

keyarg(arg1= "name", arg2="age")

##negative index
arr = [1, 2, 3, 4, 5, 6]
print(arr[-1])
print(arr[-3])

##creating class
class Interview:

    def __init__(self, emp_name):
        self.emp_name=emp_name

    def introduce(self):
        print("Hello am "+ self.emp_name)

obj=Interview("Linda")
print(obj.emp_name)
obj.introduce()

##single inheritance
class parent:
    def parent_func(self):
        print("this is from parent function")

class child(parent):
    def child_func(self):
        print("this is from child func")

obj = child()
(obj.child_func())
(obj.parent_func())

##multi level inheri
class A:
    def __init__(self, a_name):
        self.a_name= a_name

class B(A):
    def __init__(self, a_name,b_name):
        self.b_name = b_name
        A.__init__(self, a_name)
class C(B):
    def __init__(self,a_name,b_name,c_name):
        self.c_name=c_name
        B.__init__(self, a_name, b_name)
    def show_names(self):
        print(self.a_name)
        print(self.b_name)
        print(self.c_name)
obj=C("linda","vijay", "christy")
obj.show_names()

##multiple inh
class parent:
    def parent_fn(self):
        print("this is from parent")
class parent2:
    def parent2_fn(self):
        print("this is from parent2")
class child(parent, parent2):
    def show(self):
        self.parent_fn()
        self.parent2_fn()
obj=child()
obj.show()

##hierarchical
class A:
    def a_func(self):
        print("a function")
class B(A):
    def b_func(self):
        print("b function")
class C(A):
    def c_func(self):
        print("c function")
obj=C()
obj1=B()
obj.a_func()
obj.c_func()
obj1.a_func()
obj1.b_func()

##access parent member class
class parent:
    def __init__(self, name):
        self.name=name
class child(parent):
    def __init__(self, child_name, name):
        self.child_name=child_name
        parent.name=name

    def show(self):
        print("child name is", self.child_name, " and parent name is ", self.name)
obj=child("christy", "linda")
obj.show()


class Parent(object):
    # Constructor
    def __init__(self, name):
        self.name = name


class Child(Parent):
    # Constructor
    def __init__(self, name, age):
        Parent.name = name
        self.age = age

    def display(self):
        print(Parent.name, self.age)


# Driver Code
obj = Child("Interviewbit", 6)
obj.display()
##super class
class A:
    def __init__(self):
        print("this is from a")
class B(A):
    def __init__(self):
        super().__init__()
        print("this is from b")
obj=B()
##access specifiers
class Acess:
    _emp_name=None
    __age=None
    def __init__(self, emp_name, age):
        self._emp_name=emp_name
        self.__age=age
    def show(self):
        print("emp name is ",self._emp_name, " and age is " , self.__age)
ob= Acess("linda",32)
ob.show()

# to demonstrate access specifiers
class InterviewbitEmployee:
    # protected members
    _emp_name = None
    _age = None

    # private members
    __branch = None

    # constructor
    def __init__(self, emp_name, age, branch):
        self._emp_name = emp_name
        self._age = age
        self.__branch = branch

    # public member
    def display(self):
        print(self._emp_name + " " + str(self._age) + " " + self.__branch)
ob= InterviewbitEmployee("linda",32,"pcmd")
ob.display()
###empty class
class employee:
    pass
obj1=employee()
obj1.name="linda"
print(obj1.name)

class parent:
    pass
class child(parent):
    pass
obj1=parent()
obj2=child()
print(issubclass(child, parent))
print(issubclass(parent, child))
print(isinstance(obj1,child))
print(isinstance(obj1, parent))
##random numbers
import random
print(random.random())
print(random.randrange(2,10,2))
print("abdc1321".isalnum())
import re
print(bool(re.findall('[a-zA-Z0-9]+$', "abdc1321")))
##arguments
def func(*args):
    for i in args:
        print(i, end=",")
func(1)
func(1,2,3,4,5)

def check_distinct(l):
    # if len(l)== len(set(l)):
    #     return True
    # else:
    #     return False

    if len(l) == len(dict.fromkeys(l)):
         return True
    else:
        return False

print(check_distinct([1,6,5,8]))
print(check_distinct([2,2,5,5,7,8]))

from collections import Counter
import pprint
with open("2.txt","r") as file:
    data = Counter(file.read())
    form= pprint.pformat(data)
print(form)
##sum value equal to target
def find_sum(arr, n):
    visited ={}
    for i in range(len(arr)):
        target = n-arr[i]
        if target in visited.values():
            print(arr[i], target)
        else:
            visited[i]=arr[i]
    print(visited)
arr = [1, 2, 40, 3, 9, 4,0]
N = 5
find_sum(arr, N)
##add numbers without plus operator
def add(num1, num2):
    while num2 !=0:
        data = num1 & num2
        num1 = num1 ^ num2
        num2 = data << 1
    return num1
print(add(2,3))
#letter ‘a’ followed by 4 to 8 'b’s.
if re.findall('a{1}b{4,8}', ("aabbbbbc") ):
    print("yes")

date_input = "2021-08-01"
s= re.sub(r'(\d{4})-(\d{2})-(\d{2})', '\\3-\\2-\\1', date_input)
print(s)

from datetime import datetime
s = datetime.strptime("2021-08-01", "%Y-%m-%d").strftime("%d-%m-%Y")
print(s)

from collections import Counter
d1 = {'key1': 50, 'key2': 100, 'key3':200}
d2 = {'key1': 200, 'key2': 100, 'key4':300}
d3= Counter(d1)+ Counter(d2)
print(dict(d3))
print({key: d1.get(key,0)+ d2.get(key,0) for key in set(d1)| set(d2)})

##from googlesheet
from io import StringIO
import pandas
import requests
csvlink=""
data = StringIO.StringIO(requests.get(csvlink).content)
dataframe = pandas.read_csv(data)
print(dataframe.head)

def test_substring(s, substring):
    # s=s.split("s")
    # print(s)
    # for i in s:
    #     if s2[1:] in i:
    #         z="s"+i
    #         if s2 in z:
    #             print(z)
    count=0
    for i in range(len(s)):
        nxt_len = i + len(substring)
        if s[i:nxt_len]== substring:
            count +=1
    print(count)


s1 = "sdfsdfssfsdfsfsfsfgfgfagfdadssdfgsdgfdfsdfgfdfafsdgfsfsdfds"
s2 = "sdf"
print(s1.count(s2))
test_substring(s1, s2)