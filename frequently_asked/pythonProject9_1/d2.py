d1= {"Gfg" : [4, 7, 5], "Best" : [8, 6, 7], "is" : [9, 3, 8]}
K = 2
# Output : [5, 7, 8]
print([i[K] for i in d1.values()])

test_list = [{'gfg' : [5, 7, 9, 1], 'is' : 8, 'good' : 10}, {'gfg' : 1, 'for' : 10, 'geeks' : 9}, {'love' : 3, 'gfg' : [7, 3, 9, 1]}]
K = 2
key = "gfg"
for i in test_list:
    if isinstance(i[key],list):
        i[key] = i[key][K]
print(test_list)