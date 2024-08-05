sentence = 'Jim quickly realized that the beautiful Gowns are expensive'
dict1 =[]
dict=[]
for i in (sentence.split(" ")):
    if i[0].islower():
        dict1.append(i)
    else:
        dict.append(i)
# print("capital",len(dict1))
# print (len(dict))
test_dict = {1: ['gfg', 'CS', 'cool'], 2: ['gfg', 'CS']}
a={}
for i,j in test_dict.items():
    for k in j:
        # print(k)
        # print(test_dict.values())
        if k in a:
            a[k] += 1
        else:
            a[k]=1
print(a)

input = {'gfg': [5, 6, 7, 8], 'best': [6, 12, 10, 8], 'is': [10, 11, 7, 5], 'for': [1, 2, 5]}
a=[]
for i,j in input.items():
    a=a+j
l=(sorted(a))
print(set(l))
p=[]
# print(l)
print([p.append(f) for f in l if f not in p])

test_dict = {1 : ['Gfg', 'is', 'for', 'Geeks'], 2 : ['Gfg', 'is', 'CS', 'God'], 3: ['Gfg', 'best']}
dict={}
for i,j in test_dict.items():
    for k in j:
        if k in dict:
            dict[k] += 1
        else:
            dict[k]=1
print(dict)