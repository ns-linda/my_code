str1 = "James"
m=len(str1)//2
n=len(str1)
print(m,n)
res=''
res = res +str1[0] + str1[m] + str1[n-1]
print(res)

s1 = "Ault"
s2 = "Kelly"
# AuKellylt
print(s1[0:1]+s2+s1[2:])