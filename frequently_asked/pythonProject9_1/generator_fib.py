def fib(n):
    p,q=0,1
    while p<n:
        yield p
        p,q = q,p+q

x=fib(10)
for i in x:
    print(i)


