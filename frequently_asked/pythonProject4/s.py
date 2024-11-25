my_dict1 = { 'num6': 6, 'num3': 3, 'num2': 2, 'num4': 4, 'num1': 1, 'num5': 5}
sortedDict = sorted(my_dict1)
nw={}
# print(sortedDict)
for i in sortedDict:
    # print(i)
    for k,l in my_dict1.items():
        # print(l)
        if i ==k:
            nw[k] = l
# print(nw)

def find_sum(L):
    a=0
    for item in L:
        if isinstance(item, list):
            b = find_sum(item)
            a = a+b
        else:
            a= item + a
    return a

L= [1,2,[3,5],3,1]
print(find_sum(L))

a=0
def sum(l):
    for i in l:
        if isinstance(i, list):
            sum(i)
        else:
            global a
            a=a+i
    return a


L= [1,2,[3,5],3,1]

si = [i for i in L if not isinstance(i, list)]
si2 = [j for i in L if isinstance(i, list) for j in i ]
print(si2)
s=si+si2
print(sum(s))

#deco:
def inner(func):
    def square(a,b):
        a=a*a
        b=b*b
        return func(a,b)
    return square

@inner
def add(a,b):
    return a+b

print(add(2,3))

def wrapper(func):
    def change_uppercase(sentence):
        return func(sentence.upper())
    return change_uppercase

@wrapper
def sent(sentence):
    return sentence.title()

print(sent("linda is my name"))
