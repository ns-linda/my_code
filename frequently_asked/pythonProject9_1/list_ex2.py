lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
lst3=  set(lst1) & set(lst2)
print(list(lst3))
print(list(set((a) for a in lst1 if a in lst2)))


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


# Driver Code
# lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
# lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
print(intersection(lst1, lst2))

list1 = [25, 18, 9, 41, 26, 31]
list2 = [25, 45, 3, 32, 15, 20]
o=[3, 9, 15, 18, 20, 25, 25, 26, 31, 32, 41, 45]
list3 = list1 + list2
for i in range (len(list3)):
    for j in range(i+1, len(list3)):
        if list3[i] > list3[j]:
            list3[i] , list3[j]=  list3[j] , list3[i]
print(list3)

a = [[1], ['Bob'], ['Delhi'], ['x', 'y']]
print(len(a))

a=[[2, 3, 5, 8], [2, 6, 7, 3], [10, 9, 2, 3]]
s = set(a[0])
for item in a[1:]:
    print(item)
    s.intersection_update(item)
    # print(s)
print(s)
# p=[[2, 3, 5, 8], [2, 6, 7, 3], [10, 9, 2, 3]]
# result = set(p[0])
# print(result)
# for s in p[1:]:
#     result.intersection_update(s)
# print (result)



