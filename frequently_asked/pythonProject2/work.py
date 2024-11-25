s1= "abC%def&gykm"

s2= "mky%gfe&dCba"
new = [i for i in s1 if i.isalpha()]
print("".join(new[::-1]))
spec= {}
for i in s1:
    if not i.isalpha():
        spec[i]= s1.index(i)
print(spec)
