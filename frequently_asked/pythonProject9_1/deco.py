def inner(func):
    def square(a,b):
        a=a*a
        b=b*b
        return func(a,b)
    return square

@inner
def sum(a,b):
    print(a,b)
    return a+b

print(sum(2,3))

def inner1(func):
    def smart_div(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return smart_div

@inner1
def div(a,b):
    return a/b

print(div(2,4))

def inner(func):
    def square(a,b):
        a = a*a
        b = b*b
        return func(a,b)
    return square

@inner
def sum(a,b):
    return a+b

print(sum(2,5))