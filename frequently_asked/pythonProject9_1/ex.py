import re
Input=[2 , 3, 4, 5, 6]
o_P=[]
for i in range(len(Input)-2):
    z= Input[i] * Input[i+1]
    o_P.append(z)
    z = Input[i] * Input[i + 2]
    o_P.append(z)
print(o_P)

##reverse a string:
str = "a,b$c"
op=''
o=''
f= re.findall("[^a-zA-Z0-9]+", str)
for j in str:
    if  j not in f:
        op= j+op
for l,m in enumerate(str):
        if m in f:
            op=list(op)
            op.insert(l,m)
print(''.join(op))
print("########")
alpha = [i for i in str if i.isalnum()]
special = [(i,j) for i,j in enumerate(str) if not j.isalnum()]
str1= alpha[::-1]
for i,j in special:
     str1.insert(i,j)
print("".join(str1))
d={'name': ['Jan', 'Feb', 'March'], 'month': [1, 2, 3]}
d1={}
l1=[]
for i,j in d.items():
    l1.append(j)
for o in l1:
    d1
