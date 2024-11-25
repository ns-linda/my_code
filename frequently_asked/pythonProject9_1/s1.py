n = 6
def prime(n):
    for i in range(2,n):
        if n%i == 0:
            print(n, "is not a prime")
            break
    else:
            print(n," is a prime")
prime(n)