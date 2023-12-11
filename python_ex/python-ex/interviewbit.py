def print_pairs(arr, N):
    # dictionary
    num_dict = {}
    
    for num in arr:
        val = N - num
        if val in num_dict:  # check if N - num is there in dictionary, print the pair
            print("Pairs {}, {}".format(num, val))
        num_dict[num] = True
    print(num_dict)

def loops(arr, N):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == N:
                print(arr[i], arr[j])
# driver code
arr = [1, 2, 40, 3, 9, 4, 0]
N = 3
print_pairs(arr, N)
loops(arr, N)

 # global-scope variable
temp = 10 
def func():
     global temp 
     temp = 20   # local-scope variable
     print(temp)
print(temp)   # output => 10
func()    # output => 20
print(temp)   # output => 10

#decorator
def lower_case(func):
    def wrapper():
        return func().lower()
    return wrapper

def split_case(func):
    def wrapper():
        return func().split(" ")
    return wrapper

@split_case
@lower_case
def hello():
    return "HELLO WORLD"

print(hello())

##############
def cap(func):
    def wrapper(arg1, arg2):
        arg1 =arg1.capitalize()
        arg2 = arg2.capitalize()
        return func(arg1, arg2)
    return wrapper

@cap
def sent(arg1, arg2):
    return "hi "+ arg1 + " "+ arg2

print(sent("am", "linda"))
#####
mul = lambda a, b: a*b
print(mul(2,5))

def wrapper(n):
    return lambda a,b: a*b + n

mul= wrapper(5)
print(mul(2,5))
from copy import copy, deepcopy
list_1 = [1, 2, [3, 5], 4]
list3 = deepcopy(list_1)
list_2= copy(list_1)
list_2[3]=8
list_2[2].append(0)
list3[2].append(8)
print(list_1)
print(list_2)
print(list_1)
print(list3)
##############pickling########
data = {'name': 'John', 'age': 30, 'city': 'New York'}
import pickle

with open('data.pkl', "wb") as file:
    pickle.dump(data, file)

with open('data.pkl', 'rb') as file:
    l = pickle.load(file)
    print(l)
######## generators########

## generate fibonacci numbers upto n
def fib(n):
   p, q = 0, 1
   while(p < n):
       yield p
       p, q = q, p + q
x = fib(10)    # create generator object 
 
# iterating using __next__(), for Python2, use next()
print(x.__next__())    # output => 0
print(x.__next__())  
print(x.__next__())  
print(x.__next__())  
print(x.__next__())  
print(x.__next__())  
print(x.__next__())  

for i in x:
    print(i, end=" ")



