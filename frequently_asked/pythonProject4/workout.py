l1=[1, 2, 3]
l2=[9, 2, 1]
l3=l1+l2
print(l3)

for i in range(len(l3)):
    min = i
    for j in range(i+1,len(l3)):
        if l3[i] < l3[j]:
            j = min
        l3[i], l3[j] = l3[j], l3[i]

print(l3)
s1= "abC%def&gykm"
s1= "abC%def&gykm"

s2= "mky%gfe&dCba"
j=''

for i in s1:
    if i.isupper() or i.islower():
        j = str(i)+str(j)
print(j)
a=list(j)
for l, k  in enumerate(s1):
    if not k.isalpha():
        # print(k)
        a.insert(l,k)

print("".join(a))

p = [1,4,2,5,7]
for i in range(len(p)):
    min = i
    for j in range(i+1,len(p)):
        if p[i] < p[j]:
            j = min
        p[i], p[j] = p[j], p[i]
print(p)

def prime(num):
    for i in range(2, num):
        if num%i ==0:
            print(num, "is not a prime")
            break
    else:
        print(num, "is a prime")

n=10
for i in range(2,n+1):
    prime(i)



d={'a': 100, 'b':200, 'c':300}
print(sum(i for i in d.values()))

d1 = {'a': 12, 'for': 25, 'c': 9}
d2 = {'Geeks': 100, 'geek': 200, 'for': 300}
d3={}
a=0
for i in d1.keys():
    for k in d2.keys():
        if i==k:
            d2[i] = d1[i]+d2[k]
        else:
            pass
print(d2)
dict_1 = {'a': 1, 'b': 2, 'c': 3, 'x': 999}
dict_2 = {'a': 100, 'b': 100, 'c': 100, 'y': 333}

# ✅ merge dictionaries and sum key-value pairs
# (includes key-value pairs from dict_1 that are not in dict_2)
result_1 = {
    key: dict_1.get(key, 0) + dict_2.get(key, 0) for key in dict_1
}


# 👇️ {'c': 103, 'x': 999, 'a': 101, 'b': 102}
print(result_1)

# ------------------------------------------------------------------------

# ✅ merge dictionaries and sum key-value pairs (intersection)
# only includes key-value pairs that are in both dictionaries

result_2 = {
    key: dict_1.get(key, 0) + dict_2.get(key, 0) for key in set(dict_1) & set(dict_2)
}

# 👇️ {'b': 102, 'c': 103, 'a': 101}
print(result_2)

# ------------------------------------------------------------------------

# ✅ merge dictionaries and sum key-value pairs  (union)
# includes key-value pairs from both dictionaries
result_3 = {
    key: dict_1.get(key, 0) + dict_2.get(key, 0) for key in set(dict_1) | set(dict_2)
}

# 👇️ {'y': 333, 'x': 999, 'a': 101, 'b': 102, 'c': 103}
print(result_3)

# ------------------------------------------------------------------------

# ✅ merge dictionaries and sum key-value pairs
# (includes key-value pairs from dict_2 that are not in dict_1)

result_4 = {
    key: dict_1.get(key, 0) + dict_2.get(key, 0) for key in dict_2
}

# 👇️ {'a': 101, 'b': 102, 'c': 103, 'y': 333}
print(result_4)
dict_1 = {'a': 1, 'b': 2, 'c': 3, 'x': 999}
dict_2 = {'a': 100, 'b': 100, 'c': 100, 'y': 333}

# ✅ merge dictionaries and sum key-value pairs
# (includes key-value pairs from dict_1 that are not in dict_2)
result_1 = {
    key: dict_1.get(key, 0) + dict_2.get(key, 0) for key in dict_1
}


# 👇️ {'c': 103, 'x': 999, 'a': 101, 'b': 102}
print(result_1)



