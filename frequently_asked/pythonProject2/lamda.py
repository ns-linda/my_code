import functools
from functools import reduce
f = lambda x: x*x
g = lambda a, b: a+ b
print(f(5))
print(g(5,6))

nums = [2,3,4,5,6,6,7,7,8]
evens = list(filter(lambda x:x %2 ==0,nums))
print(evens)

maps = list(map(lambda x : x*2, nums))
print(maps)

reduce = reduce(lambda x ,y : x+y, maps)
print(reduce)

#find odd from list
num1 = [2, 4, 9]
num2 = [3, 8, 5]
map_example = list(map(lambda x,y : x+y, num1 , num2))
print(map_example)
#find even:
filter_ex = list(filter(lambda x : x%2 == 0, num1))
print(filter_ex)
##sum
# reduce_ex = reduce(lambda x,y : x+y, num2 )
# print(reduce_ex)
from functools import reduce
nums = [1, 2, 3, 4, 5]
summ = reduce(lambda x, y: x + y, nums)
print(summ)

lis = [1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis))