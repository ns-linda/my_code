s='geeksforgeeeks'
print("".join((set([i for i in s if s.count(i)>1]))))

s="Apple Mango Orange Mango Guava Guava Mango"
d={}
fre=1
for i in s.split(" "):
    if i in d:
        d[i] += fre
    else:
        d[i] = fre
print(d)

str = "Geeks For Geeks"
for i in str.split(" "):
    print(i, str.count(i) )

my_dict = { 'num6': 6, 'num3': 3, 'num2': 2, 'num4': 4, 'num1': 1, 'num5': 5}
sortedDict = sorted(my_dict)
print(sortedDict)
nw_dict ={}
for i in sortedDict:
    for k,l in my_dict.items():
        if i ==k:
            nw_dict[i] = l
print(nw_dict)
print(dict(sorted(my_dict.items())))
