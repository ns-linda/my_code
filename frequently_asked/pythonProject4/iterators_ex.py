class itera:
    def __init__(self, arr):
        self.arr= arr
        print(self.arr)
    def __iter__(self):
        self.pos=0
        return self

    def __next__(self):
        if len(self.arr) > self.pos:
            self.pos +=1
            return (self.arr[self.pos-1])

ob= itera([1,2,3])
it=iter(ob)
print(next(it))

from copy import deepcopy , copy
list_1 = [1, 2, [3, 5], 4]
list2=copy(list_1)
list2[2].append(5)
print(list_1)
print(list2)
list3=deepcopy(list_1)
list3[3]=9
print(list_1)
print(list3)

def wrapper(n):
    return lambda a: a*n

mul = wrapper(5)
print(mul(2))

mul = lambda a,b: a*b
print(mul(2,5))

a = [1, 2, 3]
b = [7, 8, 9]
print([x+y for x,y in zip(a,b)])

my_list = [2, 3, 5, 7, 11]
print([i**2 for i in my_list if i%2 !=0])
print({i: i**2 for i in my_list if i%2 !=0})

a=[0,1,2,3]
it=iter(a)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

