n=4
fac=1
for i in range(1,n+1):
    fac = fac * i
    print(fac)

u=9
def fib(u):
        if u==0:
           return 0
        elif u==1 or u==2:
            return 1
        else:
            return fib(u-1) + fib(u-2)
print(fib(9))