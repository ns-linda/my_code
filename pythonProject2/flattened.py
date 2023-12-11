init_dict = {'geeks': {'Geeks': {'for': 7}},
            'for': {'geeks': {'Geeks': 3}},
            'Geeks': {'for': {'for': 1, 'geeks': 4}}}
def flatten(unflattened_dict, separator='_'):
    flattened_dict = {}

    for k, v in unflattened_dict.items():
        if isinstance(v, dict):
            sub_flattened_dict = flatten(v, separator)
            for k2, v2 in sub_flattened_dict.items():
                flattened_dict[k + separator + k2] = v2
        else:
            flattened_dict[k] = v

    return flattened_dict
print(flatten(init_dict))
