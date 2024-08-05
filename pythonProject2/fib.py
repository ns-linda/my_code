def fib(n):
    if n < 0:
        print("ic")
    if n == 0:
        return 0
    elif n==1 or n == 2 :
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(9))
l= [fib(i) for i in range(1,11)]
for j in range(1,11):
    if j in l:
        print(j, " is a fib no.")
    else:
        print(j, " is not a fib no.")

def fib(n):
    if n == 0 :
        return 0
    elif n == 1 or n ==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(9))
n=4
fac=1
for i in range(1,n+1):
    fac = fac * i
    print(fac)

