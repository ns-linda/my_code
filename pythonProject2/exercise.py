s1= "abC%def&gykm"

s2= "mky%gfe&dCba"

new_list = []
spec_char = {}
for item in s1:
     if item.islower() or item.isupper():
        new_list.append(item)
     else:
        a=s1.index(item)
        spec_char[item] = a
reversed_list  =new_list [::-1]
print(reversed_list)

for i,j in spec_char.items():
    print(i,j)
    reversed_list.insert(j, i)
print(''.join(reversed_list))





l=[]
ind={}

for i in s1:
    if i.isupper() or i.islower():
        l.append(i)
    else:
        ind[i]= s1.index(i)

rev=l[::-1]
print(rev)
for j,k in ind.items():
    rev.insert(k,j)

print(''.join(rev))
