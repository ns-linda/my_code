def inner(func):
    def square(a,b):
        a=a*a
        b= b*b
        return func(a,b)
    return square

@inner
def add(a,b):
    return a+b

print(add(2,4))