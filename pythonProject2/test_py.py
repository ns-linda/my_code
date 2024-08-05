test_dict = {1: ['gfg', 'CS', 'cool'], 2: ['gfg', 'CS']}
k={}
for i in test_dict.values():
    for j in i:
        if j in k:
            k[j] += 1
        else:
            k[j] =1
print(k)

from collections import Counter
j=[]
for i in test_dict.values():
    j.extend(i)
print(Counter(j))