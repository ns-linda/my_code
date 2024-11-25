list1 = [25,4,6,7,8,2,3,4,1,9]
largest = list1[0]
for i in range(1,len(list1)):
    if largest < list1[i]:
        largest = list1[i]
print(largest)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = [i for i in list1 if i%2==0]
print(even)
