list1 = [10, 20, 5, 5, 10]
print(set(list1))
nw=[]
[nw.append(i) for i in list1 if i not in nw]
print(nw)
for i in list1:
    if i not in nw:
        nw.append(i)
print(nw)
print(list(dict.fromkeys(list1)))
