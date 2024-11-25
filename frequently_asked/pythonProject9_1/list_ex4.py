from collections import defaultdict

# The original list is : [{'is': 4, 'gfg': 2, 'best': 6}, {'it': 5, 'is': 7, 'best': 8}, {'CS': 10}]
# The merged values encapsulated dictionary is : {'is': [4, 7], 'it': [5], 'gfg': [2], 'CS': [10], 'best': [6, 8]}

l = [{'is': 4, 'gfg': 2, 'best': 6}, {'it': 5, 'is': 7, 'best': 8}, {'CS': 10}]
d=defaultdict(list)
for i in l:
    for key, value in i.items():
        print(key,value)
        d[key].append(value)
print(dict(d))

test_list1 = [5, 6, 6, 6]
test_list2 = [8, 3, 2, 9]
d= defaultdict(list)
for i,j in zip(test_list1,test_list2):
    d[i].append(j)
print(d)

l=[1,2,3,4,5]
x= sum(map(lambda x: int(x),l))
print(x)

test_list = [1, 3, 5, 5, 4, 5]

# printing original list
print("The original list is : " + str(test_list))

# value to be checked
val = 5

# initializing k
k = 3
if test_list.count(val) == k:
        print(val, "True")

