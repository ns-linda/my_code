# from itertools import count

# count=0
# my_array = [1,1,2,2,2,3,5,3,3,1,3,3,3,3,4,4,5,5,5,5,5,5,5,5,5,5]
# mac_count = {i: my_array.count(i) for i in my_array}
# print(mac_count)
# dict={}

# for i in my_array:
#     if i in dict.keys():
#         dict[i] +=1
#     else:
#         dict[i] =1
    
# print(dict)

# dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# sort, max , min on both keys and values

my_dict = {'a': 1, 'e': 0, 'b': 2, 'c': 3, 'd': 4}
# on keys
nw_dict={}
for i, j in sorted(my_dict.items()):
    nw_dict[i]=j
print(nw_dict)
print(dict(sorted(my_dict.items(), reverse =  True)))
#on values'
nw={}
values = sorted(my_dict.values())
for z in values:
    for i, j in nw_dict.items():
        if z == j:
            nw[i] = j
print(nw)
my_dict = {'a': 1, 'e': 9, 'b': 12, 'c': 3, 'd': 4}

# Sort the dictionary based on values
# sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: (item[1], item[0]))}
sorted_dict = dict(sorted(my_dict.items(), key = lambda item : item[0], reverse=True))
# Print the sorted dictionary
print(sorted_dict)
print(dict(max(my_dict.items())))
print({i:j for i,j in my_dict.items() if j == max(my_dict.values())})
print({i:j for i,j in my_dict.items() if i == max(my_dict.items())})




