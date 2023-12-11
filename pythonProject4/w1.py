l1=[1, 2, 3]
l2=[9, 2, 1]
l3=l1+l2
print(l3)

for i in range(len(l3)):
    for j in range(i+1, len(l3)):
        if l3[i] > l3[j]:
            l3[j], l3[i] = l3[i], l3[j]
print(l3)

s1= "abC%def&gykm"
a= [i for i in s1 if i.isalpha()][::-1]
for i, j in enumerate(s1):
    if not j.isalpha():
        a.insert(i,j)
print("".join(a))

def prime(n):
    for num in range(1,n+1):
            for i in range(2,num):
                if num%i == 0:
                    print(num,"not a prime")
                    break
            else:
                print(num,"prime")

prime(10)

def fib(n):
    if n==0:
        return 0
    elif n ==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(9))
n=4
fac=1
for i in range(1,n+1):
    fac =  fac*i
print(fac)

mydict={'e':5,'b':12,'a':1,'c':3}
n={}
values = sorted(mydict.values())
for i in values:
    for k,l in mydict.items():
        if l == i:
            n[k]=l
print(n)
n1={}
for i, j in sorted(mydict.items()):
    # print(i,j)
    n1[i] = j
print(n1)
test_list = [6,3,5,3]
n_l=[]
print(list(set(test_list)))
for i in test_list:
    if i in n_l:
        continue
    else:
        n_l.append(i)
print(n_l)

test_dict = {1: ['gfg', 'CS', 'cool'], 2: ['gfg', 'CS']}
n_dict={}

for j in test_dict.values():
    for i in j:
        if i in n_dict:
            n_dict[i] += 1
        else:

            n_dict[i] = 1
print(n_dict)

my_array = [1,1,2,2,2,3,5,3,3,1,3,3,3,3,4,4,5,5,5,5,5,5,5,5,5,5]
n_d={i:my_array.count(i) for i in my_array}
print(max(n_d, key= lambda x: n_d[x]))
print(max(n_d, key= n_d.get))

mydict={'e':5,'b':12,'a':1,'c':3}
nw_dict={}
for i in sorted(mydict):
    if i in mydict.keys():
        nw_dict[i]=mydict[i]
print(nw_dict)
n={}
for i in sorted(mydict.values()):
    for j,k in mydict.items():
        if i ==k:
            n[j]=k
print(n)

list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 4, 5, 1]
if len(list1) !=len(list2):
    print("not identical")
for i in list1:
        if i not in list2:
            print("not identical")
print("ïdentical")

my_array = [2, 6, 1, 7, 9, 4,1]
nw=[]
for i in my_array:
    if i in nw:
        pass
    else:
        nw.append(i)
print(nw)
n=({i:my_array.count(i) for i in my_array})
import re
string="Hello from shu.bhamg199630@gmail.com to priya@yahoo.com about the meeting @2PM"
pattern = '\S+@+\S+'
match= re.findall(pattern, string)
print(match)
string="my 1 home and 2 kids have 100 toys"
pattern = '\d+'
match= re.findall(pattern, string)
print(match)
#missing number
array=[2,1,3,6,4,7,8]
n=len(array)
total = (n+1)*(n+2)//2
sum_of = sum(array)
mis= total-sum_of
print(mis)
list = [5, 1, -96, -4, 2, 3, -1, -8, 9]
for i in range(len(list)):
    for j in range(i):
        if list[i] < list[j]:
            list[i], list[j]= list[j], list[i]
print(list)
print("smallest",list[0])
print("largest",list[-1])
myarray= "aabbccdef"
n={i:myarray.count(i) for i in myarray}
print([i for i, j in n.items() if j ==1])
