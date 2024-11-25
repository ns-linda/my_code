l =[1,2,3,6,7,8,9,5]
a=l[l.index(6):l.index(9)+1]
print(sum([i for i in l if i not in l[l.index(6):l.index(9)+1]]))
# for i in l:
#     six=l.index(6)
#     nine=l.index(9)
# # print(l[l.index(6):l.index(9)])
# for j in l[l.index(6):l.index(9)+1]:
#     l.remove(j)
#
# print(sum(l))
