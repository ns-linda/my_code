a = [10,20,30,40,50]
mul = list(map(lambda x: x*5, a))
print(mul)
print([x*5 for x in a])

li = ['The', 'quick', 'brown', 'fox', 'was', 'quick']
d={}
for i,y in enumerate(li):
    d[i]=y
print(d)

from collections import Counter
li = ['blue', 'pink', 'green', 'green', 'yellow', 'pink', 'orange']
print(Counter(li))

li = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
l2=[]
for item in li:
    l2.append(item[0])
print(l2)

a = ['w', 'x', 'y', 'z']
del a[:]
print(a)
alphabet = ['a', 'b', 'c']
integers = [15, 2, 3]
print(list(zip(alphabet, integers)))
from functools import reduce
sub= reduce(lambda x,y: x-y,integers)
print(sub)
mul=list(map(lambda x:x*5,integers ))
print(mul)
a = [-10, 27, 1000, -1, 0, -30]
filt = list(filter(lambda x: x <0,a))
print(filt)
li = [1,2,3,4,5,6,7,8,9,10]
m=list(filter(lambda x: x%2 == 0, li))
print(m)
name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
animal = ['Cat', 'Dog', 'Fish', 'Goat']
print(dict(zip(name, animal)))