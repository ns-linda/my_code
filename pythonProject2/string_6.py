s1= "abC%def&gykm"
print([i for i in s1 if i.islower()][::-1])
new_list = []
for i in s1:
    if i.islower():
        new_list.append(i[::-1])
    else:
        new_list.append(i)

print(new_list)
