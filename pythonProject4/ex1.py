sentence = 'Jim quickly realized that the beautiful Gowns are expensive'
count_upper =0
count_lower =0
d={}
count_lower = sum([count_lower+1 for i in sentence if i.islower()])
count_upper = sum([count_upper+1 for i in sentence if i.isupper()])
print(count_lower)
print(count_upper)
d['count_upper']= count_upper
d['count_lower']=count_lower
print(d)

test_dict = {1 : ['Gfg', 'is', 'for', 'Geeks'], 2 : ['Gfg', 'is', 'CS', 'God'], 3: ['Gfg', 'best']}
dict={}
for i,j in test_dict.items():
    for k in j:
        if k in dict:
            dict[k] += 1
        else:
            dict[k]=1
print(dict)
c={}
for k,l in test_dict.items():
    for m in l:
        if m in c:
            c[m] +=1
        else:
            c[m]=1
print(c)

def inner(func):
    def smart_div(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return smart_div

@inner
def div(a,b):
    return a/b

obj = inner(div)
print(obj(5,10))


def inner(func):
    def smart(a,b):
        a=a*a
        b=b*b
        return (func(a,b))
    return smart

@inner
def add(a,b):
    return a+b

print(add(2,3))














