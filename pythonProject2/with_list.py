import re
s1= "abC%def&gykm"

s2= "mky%gfe&dCba"

new_list = []
spec_char = []
for item in s1:
     if item.islower() or item.isupper():
        new_list.append(item)
     else:
        a=s1.index(item)
        spec_char.append([a,item])
reversed_list  =new_list [::-1]
print(reversed_list)

for i in spec_char:
        print((i[1]), i[0])
        reversed_list.insert(int(i[0]), i[1])
print(''.join(reversed_list))

l = [2,4,5,6,7,8]
x = list(map(lambda x: x%2 == 0, l))
print(x)

a = [1,2,3,4,5,6,7,8,9]
print(a[-1:-5])

a='csestack'
di = {}
for i in a:
    print(i)
    if i in di:
        di[i] += 1
    else:
        di[i] = 1

print({k for k,v in sorted(di.items() , key = lambda x:x[1])})

a='csestack'
b = sorted(a)
print(''.join(sorted(b , key = lambda c : b.count(c))))

str = "aabbbddeeecc"
print(list(str))
removed = list(filter(lambda x : str.count(x) %2 != 0, list(str)))
print(''.join(removed))

test_list = [5, 6, 2, 5, 3, 3, 6, 5, 5, 6, 5]
sorted_list = (sorted(test_list, key=lambda x : test_list.count(x)))
print(sorted_list)

new_l = ['a', '1', 'b', '5', 'c']
a=[]
b=[]
for i in new_l:
    if i.isalpha():
       a.append(i)
    else:
       b.append(i)
print(a)
print(b)
if len(a) != len(b):
   c=(len(a)-len(b))
   print(b)
   for i in range(0, c):
       b.append('None')

print(dict(zip(a,b)))

