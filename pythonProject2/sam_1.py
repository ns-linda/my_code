list1 = ['hi', 'this', 'is', 'a', 'very', 'simple', 'string', 'for', 'us']
list2 = [11,22,33,44,55,66,77,88,99]
list3 = []
for i in range(len(list1)):
        a=list1[i]+'_'+str(list2[1])
        list3.append(a)
print((list3))

a=lambda x,y : x + '_' + str(y)
for i in range(len(list1)):
    print(a(list1[i],str(list2[1])))

print(list(zip(list1,list2)))



