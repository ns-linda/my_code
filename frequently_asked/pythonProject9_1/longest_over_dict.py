s = "aaaaaaaaaaax"
d={}
substring=''
maxl = 0
for i in range(len(s)):
    d[i]=s[i]
    for j in range(i+1, len(s)):
        # print(s[j:])
        substring = s[i] + s[j:]
        # print(substring)
        d[-j] = substring
        # d[-j] = s[i]

# print(d)
mapx={}
for value in d.values():
    if s.count(value) > 1:
        # print(value,len(value))
        maxl = max(maxl,len(value))
print([i for i in d.values() if len(i)==maxl and s.count(i) > 1] )

