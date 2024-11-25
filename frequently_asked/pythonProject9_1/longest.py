a='geeksforgeeks'
s=''
maxl = 1
d={}
for i in range(len(a)):
    s= a[i]
    for j in range(i+1, len(a)):
        if a[j] not in s:
            s= s+ a[j]
            # print(s)
            maxl = max(maxl, len(s))
            if (maxl == len(s)):
                print(s, len(s))
print(maxl)
