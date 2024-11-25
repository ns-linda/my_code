# bubble sort
list1 = [10, 20, 5, 3, 8, 38, 52, 4, 5]
##insertion 
for i in range(len(list1)):
    for j in range(len(list1)-1):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
print(list1)
list1 = [10, 20, 5, 3, 8, 38, 52, 4, 5]
#selection
for i in range(len(list1)):
    small= i
    for j in range(i+1, len(list1)):
        if list1[small] > list1[j] :
            small = j
    (list1[i], list1[small]) = (list1[small], list1[i])
print(list1)

input = "aaabbacc"
print({i:input.count(i) for i in input})
n={}
for i in input:
    if i not in n.keys():
        n[i] = 1
    else:
        n[i] +=1
print(n)

mystr= "I love my India"
n=""
for i in mystr:
    n = i+n
print(n)

print(" ".join(i[::-1] for i in mystr.split()))

import re
str = "d 10.116.1.216 sfd 2.2.2.3 sdfsdf"
a = re.findall("\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3}",str)
print(a)

def is_valid_ipv4(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True
