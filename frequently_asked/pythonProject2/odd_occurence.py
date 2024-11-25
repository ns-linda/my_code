a=[12, 23, 34, 12, 12, 23, 12, 45]
for i in range(len(a)):
    if a.count(a[i]) % 2 ==0:
        pass
    else:
        print(a[i])