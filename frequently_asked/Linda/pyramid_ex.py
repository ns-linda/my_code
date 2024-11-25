def find_sum(lst, previous_found):
    if len(lst) > previous_found+1:
        if lst[previous_found] < lst[previous_found+1]:
            sum = lst[previous_found+1]
            index = previous_found+1
        else:
            sum = lst[previous_found]
            index = previous_found
    else:
        sum=lst  [previous_found]
        index=previous_found
    return sum, index

list_of_list = [[3], [7, 4], [2, 4, 6], [8, 9, 5, 3]]
sum_of=0
index=0
for lst in (list_of_list):
    sum, index=find_sum(lst,index)
    sum_of +=sum
print(sum_of)

mylist = [1, 1, 2, 3, 4, 5, 6]
my=dict.fromkeys(mylist)
print(list(my.keys()))

list = [3, 2, 5, 1, 8, 7]
rotation=2
for i in range(rotation):
    temp=list[0]
    for j in range(len(list)):
        if j+1==len(list):
            list[j]=temp
            break
        list[j]=list[j+1]
print(list)
list1 = [3, 2, 5, 1, 8, 7]
for i in range(rotation):
    temp=list1[len(list1)-1]
    for j in range(len(list1)-1,0,-1):
        list1[j]=list1[j-1]
    list1[0]=temp
print(list1)

def rotatestring(words,rotate):
    words=words.split()
    lengths= [len(i) for i in words]
    s = ''.join(words)
    s= s[-rotate:]+ s[:-rotate]
    # print(s)
    res=''
    i=0
    for l in lengths:
        if res:
            res+=' '
        res +=s[i:i+l]
        i+=l
    return res


print(rotatestring("my name", 1))

list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for i in range(len(list)):
    for j in range(len(list)-1):
        if list[j][1]> list[j+1][1]:
            list[j], list[j+1]=list[j+1], list[j]
print(list)

def last(n):
    return n[0]

def sorting(list):
    return sorted(list, key=last)

print(sorting(list))

def generator(n):
    number=0
    while number < n:
        yield number
        number +=1
x=generator(10)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())

dict = {'f': 1, 'e': 5, 'c': 3, 'd': 4, 'b':2}
nw={}
for i in sorted(dict):
    nw[i]=dict[i]
print(nw)
n={}
values= sorted(dict.values())
for i in values:
    for k,l in dict.items():
        if i ==l:
            n[k]=l
print(n)

import shlex
import subprocess
Host='10.204.90.31'
usr='ape'
cmd = ("ssh {0}@{1} 'ifconfig;pwd'".format(usr, Host))
subprocess.call(shlex.split(cmd))

import paramiko
ssh=paramiko.SSHClient()
connect=ssh.connect(username="", password="", hostname="")
_,stdout,_=ssh.exec_command("ifconfig")

