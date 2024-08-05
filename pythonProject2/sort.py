def sort(l1,l2):
    l3 = l1 +l2
    print(l3)
    for i in range(len(l3)):
        for j in range(i + 1, len(l3)):
            if l3[i] > l3[j]:
                l3[i], l3[j] = l3[j], l3[i]
    print(l3)
    l4 = []
    while l3:
        temp = l3[0]
        for i in l3:
            if i < temp:
                temp = i
        l4.append(temp)
        l3.remove(temp)
    return (l4)




print(sort([1,2,3],[9,2,1]))