# def flatten_dict(dd, separator='_', prefix=''):
#     '''
#     return {prefix + separator + k if prefix else k: v
#             for kk, vv in dd.items()
#             for k, v in flatten_dict(vv, separator, kk).items()
#             } if isinstance(dd, dict) else {prefix: dd}
#     '''
#     if isinstance(dd, dict):
#         for kk, vv in dd.items():
#             for k, v in flatten_dict(vv, separator, kk).items():
#                 return {prefix + separator + k if prefix else k: v}
#     else:
#         {prefix: dd}
#
# # initialising_dictionary
ini_dict = {'geeks': {'Geeks': {'for': 7}},
            'for': {'geeks': {'Geeks': 3}},
            'Geeks': {'for': {'for': 1, 'geeks': 4}}}

# # priniting initial dictionary
# print("initial_dictionary", str(ini_dict))
#
# # printing final dictionary
# print("final_dictionary", str(flatten_dict(ini_dict)))


def flatten(ini_dict, seperator = '_'):
    flat = {}
    for k, v in ini_dict.items():

        if isinstance(v,dict):
            sub_flat = flatten(v,seperator)
            for k2,v2 in sub_flat.items():
                flat[k+"_"+k2]=v2
        else:
            flat[k] = v
    return flat
print(flatten(ini_dict))


