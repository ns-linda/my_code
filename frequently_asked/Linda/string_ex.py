print("ascii value of", str(ord('A')))
print("ascci value of char is: "+ str(ord('A')))

my_array = [2, 6, 1, 7, 9, 4,9,1,1]
nw_list=[]
for i in my_array:
    if i in nw_list:
        print(i, "dups present")
    else:
        nw_list.append(i)

print(nw_list)
my_array.sort()
for i in range(len(my_array)-1):
    if my_array[i] == my_array[i+1]:
        print(my_array[i],"duplicate")
    else:
        continue

s=['abc', 'xyz', 'aba', '1221']
for i in s:
    if i[0] == i[-1]:
        print(i)

import re
string="Hello from shu.bhamg199630@gmail.com to priya@yahoo.com about the meeting @2PM"
print(re.findall('\S+@\S+', string))
print(re.findall('[0-9]+', string))
fac= 1
n=4
for i in range(1,n+1):
    fac = fac*i
print(fac)

def fac(n):
    if n ==0:
        return 1
    return n*fac(n-1)
print(fac(4))


def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fib(n-1)+ fib(n-2)
for i in range(6):
    print(fib(i), end =",")
print()
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


if __name__ == "__main__":

    n =5
    for i in range(5):
        print(fibo(i),end =",")

f=open("ex.txt",'a')
f.write("hi")
f=open("ex.txt",'r')
print(f.read())
print()

lst=[1,2,3,4,5,6,7,8]
from random import shuffle
shuffle(lst)
print(lst)

def get_missing_num(arr, n):
    total = (n +1)*(n+2)//2
    sum_of_list = sum(arr)
    return total-sum_of_list



arr = [1, 2, 3, 5]
N = len(arr)
print(get_missing_num(arr, N))