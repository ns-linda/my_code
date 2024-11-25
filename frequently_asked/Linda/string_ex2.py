def first_non_repeated_element(array):
    for i in range(len(array)):
        count=0
        for j in range(len(array)):
            if array[i]==array[j]:
                count+=1


        if count<=1:
            return array[i]


myarray= "aabbccdef"
print(first_non_repeated_element(myarray))
print([x for x in myarray if myarray.count(x)==1][0])

# num = int(input())
# get_list = list(map(int, input()))[:num]
# print(get_list)
#
# def find_largest(n):
#     larg = n[0]
#     for i in n:
#         if i > larg:
#             larg = i
#     return larg
# print(find_largest(get_list))

def square(n):
    x= lambda n : n*n

print(square(8))
