lst ="abc"
from itertools import permutations
print(list(permutations(lst)))

# n=4
# x = list(map(int,input()))[:n]
# print(x)
result=[]
def permute(data,i, len):

    if i==len:
        result.append(" ".join(data))
    else:
        for j in range(i,len):
            data[i], data[j] = data[j], data[i]
            permute(data, i+1, len)
            data[i], data[j] = data[j], data[i]
    return result
ini='abc'
print(permute(list(ini),0,len(ini)))

def inner(func):
    def smart(a,b):
        a=a*a
        b=b*b
        return func(a,b)
    return smart

@inner
def add(a,b):
    return a+b

print(add(2,3))

class Arraylist:
    def __init__(self, arr):
        self.arr= arr
    def __iter__(self):
        self.pos=0
        return self
    def __next__(self):
        if self.pos < len(self.arr):
            self.pos += 1
            return self.arr[self.pos-1]
obj= Arraylist([1,2,3])
it=iter(obj)
print(it.__next__())
print(it.__next__())
print(it.__next__())

def add(num1,num2):
    while num2 !=0:
        data= num1&num2
        num1=num1^num2
        num2=data << 1
    return num1
print(add(2,3))

