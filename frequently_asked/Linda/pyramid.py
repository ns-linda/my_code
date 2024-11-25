
def find_py(l, previous_found):
    if len(l) > previous_found+1:
        if l[previous_found] < l[previous_found+1]:
            sum = l[previous_found+1]
            index=previous_found+1
        else:
            sum = l[previous_found ]
            index = previous_found
    else:
        sum = l[previous_found]
        index = previous_found

    return sum, index

list_of_list = [[3], [7, 4], [2, 4, 6], [8, 9, 5, 3]]
sumof=0
index=0
for i in range(len(list_of_list)):
    sum, index=find_py(list_of_list[i], index)

    sumof += sum
print(sumof)


mylist = [1, 1, 2, 3, 4, 5, 6]
print(list(dict.fromkeys(mylist)))

list = [3, 2, 5, 1, 8, 7]
rotation =2
for i in range(rotation):
    temp=list[0]
    for j in range(len(list)):
        if j+1==len(list):
            list[j] = temp
            break
        list[j] = list[j+1]
print(list)
list1 = [3, 2, 5, 1, 8, 7]
rotation =2
for i in range(rotation):
    temp = list1[len(list)-1]
    for j in range(len(list1),0,1):
        list[j]=list[j-1]
    temp = list[0]
print(list)

list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for i in range(len(list)):
    for j in range(len(list)-1):
        if list[j][1] > list[j+1][1]:
            list[j], list[j+1]= list[j+1], list[j]

print(list)
