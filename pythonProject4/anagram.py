def check_ana(s1,s2):
    if sorted(s1)== sorted(s2):
        print("yes")
    else:
        print("no")

check_ana("silent", "listen")

a=['a', 1, 'b', 2, 'c', 3]
b={}
for i in range(0,len(a),2):
        b[a[i]]=a[i+1]
print(b)
d={a[i]:a[i+1] for i in range(0,len(a),2)}
print(d)

s1= "abC%def&gykm"

s3 = [i for i in s1 if i.isalpha()][::-1]
print(s3.reverse())
for i, j in enumerate(s1):
    if not j.isalpha():
        print(j)
        s3.insert(i,j)
print("".join(s3))
print(s3.sort(reverse=True))

# l=[]
# for i in s1:
#     if i.isalnum():
#         l.append(i)
lis = [i for i in s1 if i.isalnum()]
print(lis)
f=lis[::-1]
print(f)
for i, j in enumerate(s1):
    if not j.isalnum():
        f.insert(i,j)
print("".join(f))

a=[4,2,5,6,1]
print(sorted(a, reverse=True))
