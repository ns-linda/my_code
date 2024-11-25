from collections import Counter


def Diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))
    # return  [i for i in li1 if i not in li2] + [i for i in li2 if i not in li1]

def duplicates(li3):
    c= {}
    d=[]
    for i in li3:
        c[i] = li3.count(i)
    for i, j in c.items():
        if j >1:
            d.append(i)
    return d

def dup(li3):
    dup={}
    count = 1
    for i in li3:
        if i in dup:
            dup[i] = count + 1
        else:
            dup[i] = count
    return dup

def cum_sum(l4):
    l5=[]
    j=0
    for i in range(0,len(l4)):
        j =l4[i] + j
        l5.append(j)
    return l5

def chunk(my_list):
    l=[]
    for i in range(0,len(my_list),5):
        il= my_list[i: i+5]
        l.append(my_list[i: i+5])
    return l


def split(Input,length_to_split):
    for i in range(0,len(Input)):
        print(Input[i:i+length_to_split[i]])

def sortn(list3):
    a= list3[::-1]
    return a[0]

def primen(n):
    # for i in range(2,n):
    #     if n%i == 0:
    #         print(n, "not  a prime")
    #         break
    # else:
    #     print(n, "is  a prime")
    for i in range(2,n):
        if n%i==0:
            print(n, "is not a prime")
            break
    else:
        print(n, "is prime")

def fib(n):
    if n <1:
        return 0
    elif n == 1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fac(n):
    fac= 1
    for i in range(1,n+1):
        fac = fac * i
    return fac


# Driver Code
li1 = [10, 15, 20, 25, 30, 35, 40]
li2 = [25, 40, 35,100]
li3 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
l4 = [10, 20, 30, 40, 50]
my_list = ['geeks', 'for', 'geeks', 'like',
           'geeky','nerdy', 'geek', 'love',
               'questions','words', 'life']
Input = [1, 2, 3, 4, 5, 6, 7]
length_to_split = [2, 1, 3, 1]
list1 = [10, 20, 4]
# split(Input,length_to_split)
# o_p=[[1, 2], [3], [4, 5, 6], [7]]
# Output : [10, 30, 60, 100, 150]
# print(Diff(li1, li2))
# print(duplicates(li3))
# print(dup(li3))
print(cum_sum(l4))
print(chunk(my_list))
print(sortn(list1))
n= [1,2,3,4,5,6,7,8,9]
for i in n:
    primen(i)
print(fib(9))
print(fac(4))
