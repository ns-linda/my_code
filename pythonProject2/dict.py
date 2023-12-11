ini_list = [1, 2, 3, 4, 5]
new_dict = {x:'None' for x in ini_list}
print(new_dict)

test_list = [6,3,5,3]
test_dict = {'Gfg' : [5, 3, 6], 'is' : [8, 4]}
for key, value in test_dict.items():
    #print(value)
    for i in value:
        if i in test_list:
            print(key, end = " ")

test_list = ["Gfg", "is", "Best", "For", "Geeks"]

test_dict = {1: ['gfg', 'CS', 'cool'], 2: ['gfg', 'CS']}
freq = {}
for key, value in test_dict.items():
    for values in value:
        if values in freq:
            freq[values] += 1
        else:
            freq[values] = 1
print(freq)

test_list = [6,3,5,3]
test_dict = {'Gfg' : [5, 3, 6], 'is' : [8, 4]}
l=[]
for i in test_dict.values():
    for j in i:
        if j in test_list:
            l.append(j)
print(l)