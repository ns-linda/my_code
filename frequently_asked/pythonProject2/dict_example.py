Input ={
    "Key1": "Value1",
    "Key2": {
        "Key21": "Value21",
        "Key22": {
            "Key221": "Value221"
        }
    },
    "Key3": "Value31"
}
'''
Output:

{
    "Key1": "Value1",
    "Key2_Key21": "Value21",
    "Key2_Key22_Key221": "Value221",
    "Key3": "Value31, Value32"
}


def flat_dict(Input, result ={}, items = []):
        for key, val in Input.items():
            if key in result:
                 flat_dict(val, result, items + key)
            else:
                 result['_'.join(items + [key]) = val
return result
'''
init_dict = {'geeks': {'Geeks': {'for': 7}},
            'for': {'geeks': {'Geeks': 3}},
            'Geeks': {'for': {'for': 1, 'geeks': 4}}}
def flatten(current, key, result):
    if isinstance(current, dict):
        for k in current:
            new_key = "{0}_{1}".format(key, k) if len(key) > 0 else k
            flatten(current[k], new_key, result)
    else:
        result[key] = current
    return result

result = flatten(Input, '', {})
print(result)

def flatten(init_dict, seperator ="_"):
    o = {}
    for k, v in init_dict.items():
        if isinstance(v, dict):
            sub_flatten = flatten(v, seperator)
            for k2, v2 in sub_flatten.items():
                o[k + seperator + k2] = v2
        else:
            o[k] = v
    return o

print(flatten(Input))