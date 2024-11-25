test_list1 = ["gfg", 'is', 'best']
test_list2 = ['ratings', 'price', 'score']
test_list3 = [5, 6, 7]
# [{'gfg': {'ratings': 5}}, {'is': {'price': 6}}, {'best': {'score': 7}}]
dict1={}
for k in range(len(test_list2)):
    dict1[test_list2[k]]= test_list3[k]
print(dict1)
dict2={}
dict3=[]
for h in range(len(test_list1)):
    dict2[dict1.keys]=dict1.values()
    dict3.append(dict2)
print(dict3)

# dict = {}
# dict3={}
# li=[]
# for l in range(len(test_list1)):
#         dict[test_list1[l]]=dict1[l]
#
#
# print(dict)
