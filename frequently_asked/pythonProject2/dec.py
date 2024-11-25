def inner(func):
    def smart_div(a,b):
        if a < b:
            a, b = b,a
        return func(a,b)
    return smart_div

@inner
def div(a,b):
    return a/b

obj = inner(div)
print(obj(3,6))

import re
s1= "abC%def&gykm"
for i in s1:
    s2 = re.findall('\S+',i)
    print(s2)

def inner(func):
    def smart_div(a,b):
        if a <b:
            a,b = b,a
        return func(a,b)
    return smart_div

@inner
def div(a,b):
    return a/b

obj= inner(div)
print(obj(3,6))
