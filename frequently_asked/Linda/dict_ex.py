stri= "yogeshkumardewangan"
# nw_dict = {}
# for i in stri:
#     if i in nw_dict:
#         nw_dict[i] +=1
#     else:
#         nw_dict[i] =1
# print(nw_dict)

nw_dict={}
for i in stri:
    if i in nw_dict:
        nw_dict[i] +=1
    else:
        nw_dict[i]=1
print(nw_dict)
n= int(input())

p= list(map(int, input()))[:n]

print(p)
# if __name__=="__main__":
#     image_list=[]
#     dict={}
#
#     opr_count=int(input())
#
#     for _ in range(opr_count):
#         inp=input().split()
#         dict[int(inp[0])]=inp[1]
#
#     for key,value in dict.items():
#         print(str(key) + " " + value)

my_array = [1, 1, 2, 2, 2, 3, 5, 3, 3, 1, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
nw={}
print({i:my_array.count(i) for i in my_array })
print(max(my_array, key = lambda x: my_array[x]))

for i in my_array:
    if i in nw:
        nw[i] +=1
    else:
        nw[i]=1
print(max(nw))
from pip._vendor.distlib.compat import raw_input
if __name__=="__main__":
    image_list=[]
    dict={}

    opr_count=int(raw_input())

    for _ in range(opr_count):
        inp=raw_input().split()
        dict[int(inp[0])]=inp[1]
    print(dict)
    for key,value in dict.items():
        print(str(key) + " " + value)