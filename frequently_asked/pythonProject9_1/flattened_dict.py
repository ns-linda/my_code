def flattend(d,seperator="_"):
    flattened ={}
    for i, j in d.items():
        if isinstance(j,dict):
            sub_flat = flattend(j,seperator)
            for k, l in sub_flat.items():
                flattened[i+seperator+k]=l
        else:
            flattened[i]=j
    return flattened

d={'geeks': {'Geeks': {'for': 7}}, 'Geeks': {'for': {'geeks': 4, 'for': 1}}, 'for': {'geeks': {'Geeks': 3}}}
print(flattend(d))