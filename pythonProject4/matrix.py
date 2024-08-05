# def find_small(m):
#     smallest=[]
#     for i in range(row_count):
#         small = m[0][0]
#         for j in range(col_count):
#             if small > m[i][j]:
#                 smallest.append(m[i][j])
#     print(smallest)
#     print(sorted(smallest)[0])
#
# row_count=int(input())
# col_count=int(input())
# matrix=[]
# for i in range(row_count):
#     a=[]
#     for j in range(col_count):
#         a.append(int(input()))
#     matrix.append(a)
# print(matrix)
# find_small(matrix)

##palindrom of number
def find_pal(num):
    num1=num
    new_num=0
    while num > 0:
        dig= num % 10
        new_num= dig + new_num*10
        num=num //10
    if num1 == new_num:
        print("palindrome")

#permuation
result=[]
def perm(arr,index,l):
    if index ==l:
        return result.append("".join(arr))
    else:
        for j in range(index, l):
            arr[index], arr[j]= arr[j], arr[index]
            perm(arr, index+1, l)
            arr[index], arr[j] = arr[j], arr[index]
    return result
alist="abc"
a=(perm(list(alist), 0, len(alist)))
print(a)
from itertools import permutations
print(list(permutations(alist)))
#pyramid
def py(lists, previous_found):
    if len(lists) > previous_found+1:
        if lists[previous_found] < lists[previous_found+1]:
            sum = lists[previous_found+1]
            index= previous_found+1
        else:
            sum = lists[previous_found]
            index = previous_found
    else:
        sum = lists[previous_found]
        index = previous_found
    return sum, index
list_of_list = [[3], [7, 4], [2, 4, 6], [8, 9, 5, 3]]
sum_of_list=0
index=0
for lists in list_of_list:
    sum, index=py(lists, index)
    sum_of_list += sum
print(sum_of_list)
mylist = [1, 1, 2, 3, 4, 5, 6]
print(list(dict.fromkeys(mylist)))
#rotate
list = [3, 2, 5, 1, 8, 7]
rotate=2
for i in range(rotate):
    temp = list[0]
    for j in range(len(list)):
        if j+1 == len(list):
            list[j]=temp
            break
        list[j]=list[j+1]
print(list)

list=[3, 2, 5, 1, 8, 7]
rotate=2
for i in range(rotate):
    temp=list[len(list)-1]
    for j in range(len(list)-1,0,-1):
        list[j] = list[j -1]
    list[0]=temp
print(list)

##rotate string
def rotate(sentence, n):
    words=sentence.split()
    lens=[len(i) for i in words]
    s="".join(words)
    s=s[-n:]+s[:-n]
    # print(s)
    res=""
    i=0
    for l in lens:
        if res:
            res +=" "
        res += s[i:i+l]
        i+=l
    return res

print(rotate("hi am linda", 1))
list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for i in range(len(list)):
    for j in range(len(list)-1):
        if list[j][1] > list[j+1][1]:
            list[j], list[j+1]= list[j+1], list[j]
print(list)

def first(n):
    return n[0]
def sort(list):
    return sorted(list, key = first)
print(sort(list))

s="shYogeshshsh"
sub="sh"
count=0
for i in range(len(s)):
    if s[i:i+len(sub)]==sub:
        count +=1
    else:
        count = count
print(count)

class A:
    def fun(self):
        print("normal func")

def fun(self):
    print("monkey patched")
A.fun=fun
obj=A()
obj.fun()

import pickle
val=10
f=open("p.txt", "ab")
pickle.dump(val, f)
f1=open("p.txt","rb")
v=pickle.load(f1)
print(v)


