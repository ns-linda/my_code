def inner(func):
    def smart_fn(name1,name2):
        name1=name1.capitalize()
        name2 = name2.capitalize()
        return func(name1,name2
                    )
    return smart_fn

@inner
def enter(name1,name2):
    return(name1,name2)

print(enter('linda','vijay'))

my_list = [2, 3, 5, 7, 11]
d = {i:i*2 for i in my_list}
print(d)

