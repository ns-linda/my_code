from collections import defaultdict
from collections import Counter
test_dict = {1: ['gfg', 'CS', 'cool'], 2: ['gfg', 'CS']}
freq = {}
#print(freq)
for key,value in test_dict.items():
    for item in value:
        #print(item,freq)
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

#print(dict(freq))

#for key,value in test_dict.items():
    #for item in value:
        #print(Counter(value))
fre = {}
for value in test_dict.values():
    for val in value:
        if val in fre:
            fre[val] +=1
        else:
            fre[val] = 1
print(fre)

