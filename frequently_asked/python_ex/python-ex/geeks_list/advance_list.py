from asyncio.windows_events import NULL
from cgi import test


input_list = [1, 2, 2, 5, 8, 4, 4, 8]
test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
K = 3
n ={}
for i in test_list:
    if i not in n:
        n[i] = 1
    else:
        n[i] +=1
print(n)
print([i for i,j in n.items () if j >K])
test_list = [5, 6, [], 3, [], [], 9]
print([i for i in test_list if i != []])
p=[4, 5, 5, 5, 3, 8]
print([p[i] for i in range(len(p)-2) if p[i] == p[i+1] and p[i+1] == p[i+2]])

for i in range(len(p)):
    for j in range(i+1,len(p)-1):
        if p[i] == p[j]:
            print(p[i])
l=[1, 2, 3]
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j and j !=k and k !=i:
                print(l[i],l[j],l[k])

test_list = [1,2,3] 
for i in range(len(test_list)):
    print(test_list[i])

import re

size = "[13.1 GiBytes]"
size_regex = re.compile(r'^\[\d+?(\.\d+)?\s*(?:K|M|G|T)?\s*i?Bytes]$')

match = size_regex.match(size)
if match:
    print("Size string is valid:", size)
else:
    print(f"Invalid size string: {size!r}")
    if not re.search(r'\s', size):
        print("No visible spaces found.")
    else:
        print("Non-visible characters may be present. Printing repr:")
        print(repr(size))





