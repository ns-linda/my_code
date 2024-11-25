mylist = [1, 1, 2, 3, 4, 5, 6]
print(list(dict.fromkeys(mylist)))\

#anti clockwise
list = [3, 2, 5, 1, 8, 7]
for j in range(2):
    temp = list[0]
    for i in range(len(list)):
        if i+1 == len(list):
            list[i]=temp
            break
        list[i] = list[i+1]
print(list)


for j in range(2):
    temp= list[len(list)-1]
    for i in range(len(list)-1, 0, -1):
        list[i] = list[i -1]
    list[0]=temp
print(list)

import random
color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
print(random.choice(color_list))

list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# for i in range(len(list)):
#     for j in range(len(list)-1):
#         if list[j][1] > list[j+1][1]:
#             list[j], list[j+1]=list[j+1],list[j]
# print(list)

def first(n):
    return n[0]

def sort(list):
    return sorted(list, key=first)
print(sort(list))

tup = (3,4,2,7,5,6,9)
tup2= (34,454)
tup1 = tup+ tup2
print(tup1)