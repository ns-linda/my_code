# d= {'for_geeks_Geeks': 3, 'Geeks_for_geeks': 4, 'geeks_Geeks_for': 7, 'Geeks_for_for': 1}
# final_dictionary {‘Geeks’: {‘for’: {‘for’: 1, ‘geeks’: 4}}, ‘for’: {‘geeks’: {‘Geeks’: 3}}, ‘geeks’: {‘Geeks’: {‘for’: 7}}}

def nested(d,seperator = '_'):
    nested ={}
    # l=[]
    l = ([*k.split("_"), v] for k, v in d.items())
    insert(nested,l)
    return nested

def insert(nested, l):
    for x in l[:-2]:
        nested[x]=nested=nested.get(x,dict())



    # print(list(l))
d= {'for_geeks_Geeks': 3, 'Geeks_for_geeks': 4, 'geeks_Geeks_for': 7, 'Geeks_for_for': 1}
print(nested(d))