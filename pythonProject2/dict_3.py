input = {'gfg': [5, 6, 7, 8], 'best': [6, 12, 10, 8], 'is': [10, 11, 7, 5], 'for': [1, 2, 5]}
new_lis=[]
for key, value in input.items():
    for i in value:
        if i not in new_lis:
            new_lis.append(i)
print(sorted(new_lis))

test_list = [{'gfg' : 1, 'is' : 2}, {'best' : 1, 'for' : 3}, {'CS' : 2}]
new_list = []
for i in test_list:
    for key, value in i.items():
        if value not in new_list:
            new_list.append(value)
print(new_list)






