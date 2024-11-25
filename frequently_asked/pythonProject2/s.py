def sort(l1,l2):
    l3 = l1+l2
    l4=[]
    while l3:
        temp = l3[0]
        for i in (l3):
            if i < temp:
                temp = i

        l3.remove(temp)
        l4.append(temp)
    return l4


print(sort([1, 2, 3], [9, 2, 1]))

l1=[1, 2, 3]
l2=[9, 2, 1]
l3=l1+l2
l3.sort()
print(l3)

for i in range(len(l3)):
    minid_x = i
    for j in range(i+1, len(l3)):
        if l3[i] < l3[j]:
            minid_x = j

        l3[minid_x], l3[j] = l3[j],   l3[minid_x]

print(l3)