
def st(sort_list):
    sort_list.sort(key = lambda x : x[1])
    print(sort_list)


sort_list= [['rishav', 10], ['akash', 5], ['ram', 20], ['gaurav', 15]]
st(sort_list)


my_list = [-15, -26, 15, 1, 23, -64, 23, 76]
for i in range(len(my_list)):
    for j in range(i+1, len(my_list)):
        if my_list[i] > my_list[j]:
            my_list[i], my_list[j] = my_list[j], my_list[i]

print(my_list)
my_list.sort(key = lambda x:x, reverse=True)
print(my_list)


def return_first(k):
    a=[]
    for i in k:
            a.append(i[0])
    print(a)
k=[[1, 2], [3, 4, 5], [6, 7, 8, 9]]
return_first(k)
print("####")
print([j for i in k for j in i if i.index(j) ==0])

def Extract(lst):
    return [item[0] for item in lst]
# Driver code
lst = [[1, 2], [3, 4, 5], [6, 7, 8, 9]]
# print[lambda x : (i[0] for i in lst)
print(Extract(lst))

result = map(lambda x: x[0] , lst)
print(list(result))

arr1 = [1, 3, 4, 5, 7]
arr2 = [2, 3, 5, 6]
print(list(i for i in arr1 if i in arr2))

Input = [1, 2, 3, 2, 3, 1, 3,5,5,5,6,7,7,7,1]
a= set((i for i in Input if Input.count(i)%2 !=0))
print(list(a))

l_e=[[1, 2, 3], [4, 5], [6, 7, 8, 9]]
d=list(map(lambda x: x[-1], l_e))
print(d)
s=[]
for i in l_e:
    a = lambda i : i[-1]
    s.append(a(i))
print(list(s))

print(list(i[-1] for i in l_e))
