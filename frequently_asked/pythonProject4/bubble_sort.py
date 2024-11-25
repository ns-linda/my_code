a=[32,5,3,6,7,54,87]
for i in range(len(a)-1,0,-1):
    for j in range(i):
        # print(j)
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] =a[j+1]
            a[j+1]=temp
print(a)

for i in range((10)):
        print((9-i)*" "+i*"* "+" " )

def fib(n):
    p,q=0,1
    while p <n:
        yield p
        p,q = q, p+q

x=fib(10)
for i in x:
    print(i)

def prime(n):
    for i in range(1,n):
        for j in range(2,i):
            if i%j == 0:
                print(i," Not a prime")
                break
        else:
            print(i, "is a prime")
prime(10)

list = ["1", "4", "0", "6", "9"]
a= [int(i) for i in list]
print(a)
def sort(a):
    for i in range(len(a)):
        for j in range(i):
            if int(a[i]) < int(a[j]):
                a[j], a[i] = a[i], a[j]

sort(a)
print(a)

# print(list)
