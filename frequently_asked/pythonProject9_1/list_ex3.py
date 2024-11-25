lst1 = [[1, 'Alice'], [2, 'Bob'], [3, 'Cara']]
lst2 = [[1, 'Delhi'], [2, 'Mumbai'], [3, 'Chennai']]

for i in range(len(lst1)):
    for j in lst2:
        if lst1[i][0] == j[0]:
            lst1[i].append(j[1])
print(lst1)


ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
s1=set(ar1)
s2=set(ar2)
s3=set(ar3)
s1.intersection_update(s2,s3)
print(s1)

l1=[5, 6, 10, 4, 7, 1, 19]
l2= [6, 6, 10, 3, 7, 10, 19]
sum1=0
a = sum((sum1+1) for i in l1 if i in l2)
print((a))
s3= set(l1)& set(l2)
print(len(s3))
sum2=0
s1 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
s2 = sum((sum2+1) for i in s1 if isinstance(i, list) )
print(s2)
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
print([i for i in list1 if i in list2])
# print(x)

l1 = [['+', '-', '+'], ['-', '+'], ['+', '-', '+']]
l2 = [['2a3', 'b2', '3c'], ['a3', 'b2'], ['a3', '2b2', '5c']]
o=[['+2a3', '-b2', '+3c'], ['-a3', '+b2'], ['+a3', '-2b2', '+5c']]

l4=[]
for i, j in zip(l1,l2):
    # print(i,j)
    l3 = []
    for x, y in zip(i,j):
        z=x+y
        l3.append(z)
    l4.append(l3)

print(l4)


v= [[i+j for i, j in zip(x,y)]for x,y in zip(l1,l2)]
print(v)

lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
# print(l3)
l3=[]
for k,l in zip(lst1,lst2):
    l3.append(k)
    l3.append(l)
    # l3.append(z)
# print(l3)
from collections import defaultdict
test_list1 = [0, 0, 0, 1, 1, 1, 2, 2]
test_list2 = ['gfg', 'is', 'best', 'Akash', 'Akshat', 'Nikhil', 'apple', 'grapes']
res = defaultdict(list)
for i, j in zip(test_list1, test_list2):
    print(i,j)
    res[i].append(j)
print(dict(res))


