gfg = "geeksforgeeks"
print(reversed(gfg))
print(gfg[::-1])

k= {'a': 100, 'b':200, 'c':300}
a=0
for i, j in k.items():
    a=a+j

print(a)

test_dict = {'Gfg': 1, 'is': 2, 'best': 3, 'for': 4, 'CS': 5}

# initializing Remove keys
rem_list = ['is', 'for', 'CS']
new_dict ={}
for i, j in test_dict.items():
    if i not in rem_list:
            new_dict[i] = j
print(new_dict)

f= {'geeksforgeeks' : 1, 'practice' : 2, 'contribute' :3}
keys = ['geeksforgeeks', 'practice']
for i in keys:
    if i not in f.keys():
        print("False")
    else:
        print("True")
test_dict = {"Gfg" : 1, "is" : 2, "Best" : 3}
l=[]
for i,j in test_dict.items():
    l.append(i)
    l.append(j)
print(l)
#### sorting on keys
my_dict = {'c':3, 'a':1, 'd':4, 'b':2}
y_dict ={}
for i, j in sorted(my_dict.items()):
    y_dict[i] = j

print(y_dict)

#### sorting on values
sorted_values = sorted(my_dict.values())
sort_v_dict={}
for k in sorted_values:
    for l,m in my_dict.items():
        if k == l:
            sort_v_dict[l] = m
print(sort_v_dict)

l = [2,3,4,5,1,4,2]
l.sort(reverse=True)
print(l)
print(l[::-1])
a=sorted(l)
a.reverse()
print(a)

###########decorator

def square(func):
    def smart_func(a,b):
        a, b = a*a, b*b
        return func(a,b)
    return smart_func

@square
def add(a,b):
    return a+b

obj = add(2,3)
print(obj)

####
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]
new={}

def print_range(initial, end):
    if initial <= end :
        # print(initial)
        print_range(initial+1, end)
print_range(1,100)

def pp(n):
    if n >=1:
        pp(n -1)
        print(n, end = ', ')


(pp(2))
