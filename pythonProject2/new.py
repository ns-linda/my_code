def find_sum(L):
    a=0
    for item in L:
        if isinstance(item, list):
            print(item)
            b = find_sum(item)
            print(b)
            a= a+b
        else:
            a = item + a
    return a

L= [1,2,[3,5],3,1]
# print(find_sum(L))
sum =0
for i in range(len(L)):
    # print(type(L[i]))
    if  type(L[i]) != list:
        sum = sum + L[i]
        # print(sum)
    else:
        for j in range(len(L[i])):
            print(j)
            sum = sum + L[j]
# print(sum)
    # print((i))


# def square(func):
#     def sq(a,b):
#         c =a*a + b*b
#         return ()
#     return square()
#
# @square
# def add(a,b):
#     return a+b

# obj = square()

k = [1,5,6,2,1,6,8,4,2]
# k= list(set(k))
# k.sort()
# print(k[1])

# for i in range(len(k)):
#     min_id = i
#     for j in range(i+1,len(k)):
#         if k[i] > k[j]:
#             i=j
#         k[min_id], k[i] = k[i], k[min_id]
# print(k)
#
# # z= "Python"
# # for i in
# # i[0] = "z"
# #
# # z.replace("P")
# # for i in z:
# #     if i.islower():
# #         print()
#
# z="python"
# print(z[0].capitalize()+z[1:].lower())
# print(z[0].replace("p","z")+z[1:].lower())
#
#
# class S:
#     a = 1
#
#     def __init__(self):
#         self.b = 2
#
#
# obj = S()
# value = S().b
# print(value)
# value_1 = obj.a
# print(value_1)
#
# class emp:
#
#     def __init__(self):
#         self.a =10
#
#     def display(self):
#         print("hi")
#
# class emp_1(emp):
#
#     def display(self):
#         super().display()
#
#
# obj = emp_1()
# obj.display()
#
#
# mydict={'e':5,'b':12,'a':1,'c':3}
# #{'a': 1, 'c': 3, 'e': 5, 'b': 12}
# sorted_v = sorted(mydict.values())
# new_dict={}
#
# for i in sorted_v:
#     for j in mydict.keys():
#         if mydict[j] == i:
#             new_dict[j] = i
# print(new_dict)
