def inner(func):
    def smart_div(a, b):
        if a < b:
            a, b = b, a
        return func(a,b)
    return smart_div
@inner
def div(a, b):
    print(a/b)

obj = inner(div)
obj(3,6)

# def make_pretty(func):
#     def inner():
#         print("Iam decorated")
#         func()
#     return inner()
#
# @make_pretty
# def ordinary():
#     print("Iam ordinary")
#
# obj1=make_pretty(ordinary)
#











# def make_pretty(func):
#
#     def inner(func):
#         print("am decorated")
#     return inner
# @make_pretty
# def original():
#     print("am original")
#
# print(make_pretty(original))

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)

obj = smart_divide(div)
obj(3,6)