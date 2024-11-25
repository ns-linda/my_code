import array

arr = array.array('i',[1,2,3,4])
arr.append(5)
print(arr)

a= lambda x,y : x+y
print(a(1,2))

import array

arr = array.array('i', [1, 2, 3, 2])

print(arr)

for i in range(len(arr)):
    print(arr[i])

arr.append(5)
print(arr)

# lambda

a = lambda x, y: x + y
print(a(2, 3))