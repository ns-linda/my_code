test_dict = {'Manjeet': 1, 'Nikhil': 1, 'Akash': 2, 'Akshat': 3}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

flag = False
hash_val = dict()
for keys in test_dict:
    print(keys, test_dict[keys])
    if test_dict[keys] in hash_val:
        flag = True
        break
    else:
        hash_val[test_dict[keys]] = 1

# print result 
print("Does dictionary contain repetition : " + str(flag))
print(hash_val)

test_dict = {1 : ['Gfg', 'is', 'for', 'Geeks'], 2 : ['Gfg', 'is', 'CS', 'God'], 3: ['Gfg', 'best']}
new_list = []
count = 0
fd={}
for value in test_dict.values():
    for val in value:
        if val.startswith('G'):
            new_list.append(value)
            count += 1
            fd[val] = count
print(fd)
n=[]
e={}
count =0
for value in test_dict.values():
    n.extend(value)
for value in n:
    if value in e:
        e[value] += 1
    else:
        e[value] = 1
print(e)


