from functools import reduce
List = [23, 65, 19, 90]
pos1 = 1
pos2 = 3
temp = List[pos1-1]
List[pos1-1] = List[pos2-1]
List[pos2-1] = temp
print(List)

list1 = [1, 2, 3,9]
i=1
for j in list1:
    x=i*j
    i=x
print(x)

res1 = reduce((lambda x , y :x*y),list1)
print(res1)