str1 = "Analytics Vidhya"
str2=''
for i in str1:
    str2 = i + str2
print(str2)

d = {'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}
# The unique values list is : [1, 2, 5, 6, 7, 8, 10, 11, 12]
n=[]
for i in d.values():
    for j in i:
        if j not in n:
            n.append(j)
print(n) 
for i, j in d.items():
    for z in j:
        if z not in n:
            n.append(z)
n.sort()
print(n)

dict = {'a': 100, 'b': 200, 'c': 300}
n=0
print(sum([n+i for i in dict.values()]))

##pattern
for i in range(0,10):
    for j in range(0,i+1):
        print("* *", end =" ")
    print("\r")
    

import re
input = '657'
pattern  = '^[78653]'
if re.match(pattern, input):
    print("match")
    
a = "ThisIsGeeksforGeeks!, 123"
upper = re.findall(r'[A-Z]',a )
lower = re.findall(r'[a-z]',a )
digits=re.findall(r'[0-9]',a )
print("uppercase: ", len(upper))
print("lowercase: ", len(lower))
print("digits: ", len(digits))

b= 'geek55of55geeks4abc3dr2' 
number = re.findall(r'[0-9]+', b)
print(number)


def swaplist(l):
    l[0], l[-1] = l[-1], l[0]
    return l
print(swaplist([12, 35, 9, 56, 24]))

str = "geeksforgeeks"
k = 2
d={}
for i in str:
    if i not in d:
        d[i] = 1
    else:
        d[i] +=1
f = {i:j for i,j in d.items() if j ==1}
element = list(f.items())[k-1]
print(element)

test_list = [2, 3, 5, 6, 2, 6, 8, 9, 4, 6, 1]
# test_list =  [2, 3, 5, 6, 2, 6, 8]
K = 6
n = []
p = 0
# Output : [10, 6, 2, 6, 21, 6, 1] 
for i in test_list:
    if i != K:
        p +=i
    else:
        n.append(p)
        n.append(K)
        p=0
n.append(i)
print(n)

# Add
def pnos(n):
    if n >0:
        print(n, end = " ")
        pnos(n-1)
pnos(100)
print()
print()
# s = "geeks123available"
s = "98apple658pine"
# Output : ('available', 123)
import re
digits = re.findall('\d+',s)
print(digits)
maxd = max((digits), key =len)
letters = re.findall('[a-z]+', s)
maxl = max((letters), key =len)
print(maxd, maxl)

h = "geeks"
k = 1
n={}
for i in range(len(h)):
    substring = h[:i] + h[i+1:]
    if len(substring) == len(h)-k and substring not in n:
        n[substring] = len(substring)  
print(n)

inp = "ThisIsGeeksforGeeks!, 123" 
pattern = "[!@#$%^&*()_+~,]"
uppercase =  re.findall("[A-Z]", inp)
lowercase =  re.findall('[a-z]', inp)
digits = re.findall('\d', inp)
special = re.findall(pattern, inp)
print(lowercase)
print(uppercase)
print(digits)
print(special)

inp = "geek55of55geeks4abc3dr2" 
digit = re.findall(r"[0-9]+", inp)
data = {i:inp.count(i) for i in digit} 
print(max(data))
    
inp="BruceWayneIsBatman"
print("".join([f' {i}' if i.isupper() else i for i in inp ]))
out=""
for i in inp:
    if i.isupper() and inp.index(i) !=0:
        out +=" "+i
    else:
        out +=i
print(out)

inp = "100klh564abc365bg"
digits = re.findall("\d+", inp)
print(digits)
# maxl = max((digits), key = len)
print(max(digits))

inp = "abba"
print("valid" if i[0]==i[-1] else "invalid")

initial_string =" abcjw:, .@! eiw"
chars = re.findall("[a-z]", initial_string)
print("".join(i for i in chars))
        
# end_digits = "ankitrai326"
end_digits = "ankirai@"
print("valid" if re.findall("\d$", end_digits) else "Invalid")

Input = "animal"
pattern = "^[aeiou]"
if re.search(pattern, Input):
    print("yes")
