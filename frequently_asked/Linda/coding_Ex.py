a='%python123%$#'
import re
pat = re.findall('[a-zA-Z]',a)
print(len(pat))
pat1=re.findall('[0-9]',a)
print(len(pat1))
pat2=re.findall('\W',a)
print(len(pat2))

s='quescol'
o=re.sub('e','',s)
print(o)

s='ques ol'
pat=re.sub(' ','c',s)
print(pat)
print(s.replace(" ", 'c'))

s='Quescol'
print(s.upper())

s='Quescol'
vowels = 'aeiou'
n=""
for i in s:
    if i in vowels:
        pass
    else:
        n +=i
print(n)
resut=s
print(s)
astring = "".join([ i for i in s if i not in vowels])
print(astring)
s='Quescol'
vowels=[i for i in s if i in vowels]
cons = [i for i in s if i not in vowels]
print(len(vowels))
print(len(cons))
s='Quescol'
d={key : s.count(key) for key in s}
print(max(d, key= lambda x:d[x]))

v = [i for i in s if i in vowels]
print(s.replace(v[0],'-'))

# s="am linda catherine"
# p= re.sub(' ', '',s)
# print(p)
# str1=input()
# str2=input()
# print("".join([str1,str2]))

s='aaabaabc'
n=''
for i in s:
    if i not in n:
        n +=i
print(n)

s='amb324kl98'
o=re.findall('[0-9]',s)
print(sum(int(i) for i in o))

s='aaabcffgh'
print("".join([i for i in s if s.count(i)==1]))
n=""
for i in s:
    if i not in n:
        n+=i

arr = [1, 2, 40, 3, 9, 4,0, 5]
N = 5
d={}
for i in range(len(arr)):
    val = N-arr[i]
    if val in d:
        print(val, arr[i])
    else:
        d[i]=i
arr=[2, 3, 4, 5, 6, 6]
smallest = arr[0]
largest = arr[0]
for i in range(len(arr)):
    if smallest > arr[i]:
        smallest = arr[i]
    if largest < arr[i]:
        largest = arr[i]
print(smallest)
print(largest)
r=[]
for i in range(len(arr)-1,-1,-1):
    r.append(arr[i])
print(r)
arr.pop()
print(arr)

##left rotation
rotation=2
for i in range(rotation):
    temp = arr[0]
    for j in range(len(arr)):
        if j+1==len(arr):
            arr[j]= temp
            break
        arr[j]=arr[j+1]
print(arr)

def capitalize(func):
    def wrapper():
        return func().upper()
    return wrapper

@capitalize
def char():
    return "hi, this is linda"

print(char())

def inner(func):
    def wrapper(a,b):
        a=a**2
        b=b**2
        return func(a,b)
    return wrapper

@inner
def add(a,b):
    return a+b
print(add(2,3))

def add(num1, num2):
    while num2 !=0:
        data= num1 & num2
        num1 = num1 ^ num2
        num2 = data << 1
    return num1

print(add(2,3))

def print_pairs(arr, N):
    visited={}
    for i in range(len(arr)):
        val=N-arr[i]
        if val in visited.values():
            print(val, arr[i])
        else:
            visited[i]=arr[i]
    print(visited)

arr = [1, 2, 40, 3, 9, 4,0]
N = 3
print_pairs(arr, N)

##bubble sort
lis = [3, 2, 5, 1, 8, 7]
rotation=2
for i in range(rotation):
    temp=lis[0]
    for j in range(len(lis)):
        if j+1==len(lis):
            lis[j]=temp
            break
        lis[j]=lis[j+1]
print(lis)
lis = [3, 2, 5, 1, 8, 7]
#clock
for i in range(rotation):
    temp=lis[len(lis)-1]
    for j in range(len(lis)-1,0,-1):
        lis[j]=lis[j-1]
    lis[0]=temp
print(lis)

def rot_string(words, r):
    words = words.split()
    lengths = [len(w) for w in words]
    s = ''.join(words)
    s = s[-r:] + s[:-r]
    res = ''
    i = 0
    for l in lengths:
        if res:
            res += ' '
        res += s[i:i + l]
        i += l
    return res


print(rot_string("hi am linda", 1))
result=[]
def perm(arr,i,l):
    if i == len(arr):
        result.append("".join(arr))
    else:
        for j in range(i,l):
            arr[i], arr[j]=arr[j], arr[i]
            perm(arr, i+1, l)
            arr[i], arr[j] = arr[j], arr[i]
    return result

ini_str = "abc"
print(perm(list(ini_str),0, len(list(ini_str))))

##bubble
arr=[4,6,3,2,8,1]
for i in range(len(arr)-1,0,-1):
    for j in range(i):
        if arr[j]> arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(arr)

for i in range(len(arr)):
    for j in range(i+1):
        if arr[i]< arr[j]:
            arr[i], arr[j]=arr[j], arr[i]
print(arr)






