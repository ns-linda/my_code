from collections import Counter

d1 = {'key1': 50, 'key2': 100, 'key3':200}
d2 = {'key1': 200, 'key2': 100, 'key4':300}
d3= Counter(d1)+ Counter(d2)
print(dict(d3))
print(d2.get('key4'))
d4 = {key : d1.get(key,0)+ d2.get(key,0) for key in set(d1)|set(d2)}
print(d4)
d5=set(d1)|set(d2)
print((d5))
for key  in d5:
    key = d1.get(key,0) + d2.get(key,0)
    
test_list = [{'gfg' : 3, 'is' : 7}, {'gfg' : 3, 'is' : 1, 'best' : 5}, {'gfg' : 8}]
keys_list = [i for keys in test_list for i in keys ]
a=list(set(keys_list))
print(a)
for k in range(len(test_list)):
    for i in a:
        if i not in test_list[k]:
            test_list[k][i]=None
        else:
            pass
            # print(i, test_list[k])
            # test_list[k].update(i ='None')
print(test_list)
from functools import reduce
dict = {'value1':5, 'value2':4, 'value3':3, 'value4':2, 'value5':1}
mul=1
print( reduce((lambda x,y : x*y ), dict.values()))

test_dict = {'Gfg': 3, ' is ': 5, 'for ': 8, 'Geeks': 10, 'Best': 16}
sub_list = [5, 4, 10, 20, 16, 8]
nw={}
for i,j in test_dict.items():
    if j in sub_list:
        nw[i] = j
print(nw)

d1 = {'key1': 50, 'key2': 100, 'key3':200}
d2 = {'key1': 200, 'key2': 100, 'key4':300}
print({i: d1.get(i,0)+ d2.get(i,0) for i in set(d1) | set(d2)})


d1 = {'key1': 50, 'key2': 100, 'key3':200}
d2 = {'key1': 200, 'key2': 100, 'key4':300}
d3={}
print(set(d1) | set(d2))
print({key: d1.get(key,0)+d2.get(key,0) for key in set(d1) | set(d2)  })
print({key : d1.get(key,0)+ d2.get(key,0) for key in set(d1)|set(d2)})
print(dict(zip(d1.items(),d2.items())))

for i, j in d1.items():
    if i in d2.keys():
        d3[i]= j + d2[i]
if d2.keys() not in d1.keys():
    print(d2.keys())
