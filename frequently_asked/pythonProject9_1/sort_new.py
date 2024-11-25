a = [2, 64, 25, 12, 22, 11]
# A.sort()
# print(A)
# print(sorted(A))
# print(b)
# for i in range(len(A)):
#     min_idx = i
#     for j in range(i+1, len(A)):
#         if A[i] > A[j]:
#             i = j
#
#     A[i], A[min_idx] = A[min_idx], A[i]
#
# print(A)
#
# for i in range(len(A)):
#     min_id = i
#     for j in range(i+1, len(A)):
#         if A[i] > A[j]:
#             i=j
#     A[i], A[min_id] =  A[min_id], A[i]
#
# print(A)
#
#

for i in range(len(a)-1,0,-1):
    for j in range(i):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
print(a)

for k in range(len(a)):
    for l in range(k+1, len(a)):
        if a[k] > a[l]:
            a[k], a[l]= a[l], a[k]
print(a)

def fib(n):
    p,q = 0,1
    while p < n:
        yield p
        p, q = q, p+q
x=fib(10)
for i in x:
    print(i)

fac=1
for i in range(1,5):
    fac = fac * i
print(fac)

for i in range(1, 10):
    for j in range(2, i):
        if i%j ==0:
            print(i, "not a prime")
            break
    else:
        print(i, "is prime")



