# def gen(n):
#     i =0
#     while i <n:
#         yield i
#         i = i+1
#
# n=gen(10)
# for i in (n):
#     print(i, end =",")
#
# def fib(n):
#     p,q=0,1
#     while p < n:
#         yield p
#         p,q = q, p+q
# x=fib(10)
# for i in x:
#     print(i, end =",")
#
#
# def number(n):
#     i=0
#     while i<n:
#         yield i
#         i=i+1
#
# n=11
# x=number(n)
# print(next(x), end=", ")
# for i in x:
#     print((i), end=", ")


def fib(n):
    p,q = 0,1
    while p < n:
        yield p
        p,q= q,p+q

x=fib(10)
for i in x:
    print(i, end=", ")
print()
def num(n):
    i=0
    while i < n:
        yield i
        i=i+1
x=num(10)
# for i in x:
#     print(i, end=
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
# print(next(x))

def print_num(i, l ):
    if i < l:
        print(i, end=", ")
        print_num(i+1, l)

print_num(1,11)

start = -4
end = 5
for i in range(start, end):
    if i >=0:
        print(i)
