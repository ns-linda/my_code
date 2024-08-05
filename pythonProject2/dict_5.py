from collections import Counter
from collections import defaultdict
from itertools import permutations
test_list = [{"Gfg" : 6, "is" : 9, "best" : 10},
             {"Gfg" : 8, "is" : 11, "best" : 19},
             {"Gfg" : 2, "is" : 16, "best" : 10},
             {"Gfg" : 12, "is" : 1, "best" : 8},
             {"Gfg" : 22, "is" : 6, "best" : 8}]
new_dict = defaultdict(list)
new_list = defaultdict(list)
for sub in test_list:
    for key in sub:
        new_dict[key].append(sub[key])
print(new_dict)

str =  [1, 1, 1, 64, 23, 64, 22, 22, 22]
print(Counter(str))

for key, val in  Counter(str).items():
    if val == 3:
        print(key , val)
for i in range(len(str)-2):
    if str[i] == str[i+1] and str[i+1] == str[i+2]:
        print(str[i])

str = "geeksforgeeks"
k = 3
print(str[k])

N = 3
K = 4
l=[]
for i in range(1,N+1):
    l.append(i)
x=permutations(l)
print(x)
for t in list(x):
    print(t)