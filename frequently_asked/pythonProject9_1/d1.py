from audioop import mul


d1={'a': 100, 'b':200, 'c':300}
print(sum(j for i,j in d1.items()))

dict1 = {'value1':5, 'value2':4, 'value3':3, 'value4':2, 'value5':1}
ans=1
print([l*ans for k,l in dict1.items()])

test_list = [{"Gfg" : 3, "is" : 9, "best" : 10}, {"Gfg" : 8, "is" : 11, "best" : 19}, {"Gfg" : 9, "is" : 16, "best" : 1}]
K = "best"
o = "is"
maxl=1
# Output : 11
# for p in test_list:
#     for t,m in p.items():
#         if t == K :
#             maxl = max(maxl,m)
# print(maxl)
# for p in test_list:
#     for t,m in p.items():
#         if p[K] == maxl:
#             print(p[o])
# for item in test_list:
#     for t, m in item.items():
#         if t == K :
#             maxl = max(maxl,m)
res = max(test_list, key=lambda ele: ele.get(K, 0)) 

# printing result
print("The required value : " + str(res))
            
test_dict = {"Gfg" : [6, 7, 3, 1], "is" : [9, 1, 4], "best" : [10, 7, 4]}
K = "Gfg"
l = 1
# Output : 7
for i,j in test_dict.items():
    if i ==K:
        print(j[l])
temp = test_dict.get(K)
print([i for i in temp if temp.index(i) ==l])

##to find element
Tv = {'BreakingBad':100, 'GameOfThrones':1292, 'TMKUC' : 88}
maxkey = max(Tv, key=lambda x:Tv[x] )
maxi=max(Tv.values())
print("".join([i for i,j in Tv.items() if j == maxi]))

print(maxkey)
from functools import reduce
print("################")
d1={'a': 100, 'b':200, 'c':300}
print(sum(d1.values()))
dict1 = {'value1':5, 'value2':4, 'value3':3, 'value4':2, 'value5':1}
print(reduce(lambda x, y : x*y, dict1.values()))
mul=1
for i in dict1.values():
    mul = mul * i
print(mul)
test_list = [{"Gfg" : 3, "is" : 9, "best" : 10}, {"Gfg" : 8, "is" : 11, "best" : 19}, {"Gfg" : 9, "is" : 16, "best" : 1}]
out = max(test_list, key = lambda ele:ele.get(K,0))
print(out)
Tv = {'BreakingBad':100, 'GameOfThrones':1292, 'TMKUC' : 88}
out = max(Tv, key = lambda x:Tv[x])
print(out)
print(max(Tv))
