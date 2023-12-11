test_str = "ababa"

# Output : {‘a’: 3, ‘ab’: 2, ‘aba’: 2, ‘abab’: 1, ‘ababa’: 1, ‘b’: 2, ‘ba’: 2, ‘bab’: 1, ‘baba’: 1} 
print([test_str.count(i) for i in test_str])
n=[]
d={}
freq = 1
for i in range(len(test_str)):
    for j in range(i+1, len(test_str)+1):
        n.append(test_str[i:j])
for i in n:
    if i not in d.keys():
        d[i] = freq
    else:
        d[i] += freq
print(d)
print([test_str[i:j] for i in range(len(test_str)) for j in range(i+1, len(test_str) + 1)])

test_list1 = ["Gfg", "is", "Best"]
test_list2 = ["I love Gfg", "Its Best for Geeks", "Gfg means CS"]
print([True if  i in ' '.join(test_list2) else False for i in test_list1])
n=[]
for i in test_list1:
    if i in test_list2:
        n.append(True)
    else:
        n.append(False)
print(n)

from ast import arg
import re
g = 'geeksgeeks are geeks for all geeksgeeksgeeks'
substr="geeks"
# The maximum run of Substring : geeksgeeksgeeks
res = re.findall(f"(?={re.escape(substr)})", g)
print(res)

test_str = "geksefokesgergeeks"
arg_str = "geeks"
# Python3 code to demonstrate working of 
# Possible Substring count from String
# Using min() + list comprehension + count()

# initializing string
test_str = "gekseforgeeks"

# printing original string
print("The original string is : " + str(test_str))

# initializing arg string 
arg_str = "geeks"

# using min and count to get minimum possible 
# occurrence of character
res = (test_str.count(char) // arg_str.count(char) for char in set(arg_str))

# printing result 
print("Possible substrings count : " + str(res)) 
for char in set(arg_str):
    print(test_str.count(char))
    # print(arg_str.count(char))
    # print(test_str.count(char) // arg_str.count(char))

test_str = "geksefokesgergeeks"
arg_str = "geeks"
n={}
arg_stri = set(arg_str)
res = min(test_str.count(char) // arg_str.count(char) for char in arg_stri)
print(res)

test_str = 'geeksforgeeks' 
s1 = 'geeks' 
s2 = 'abcd'
a =re.sub(s1,s2,test_str)
print(a)
g=test_str.split(s1)
r=''
for i in g:
    if i =='':
        r += s2
    else:
        r +=i
print(r)

# Python3 code to demonstrate working of 
# Longest Substring of K
# Using loop

# initializing string
test_str = 'abcaaaacbbaa'

# printing original String
print("The original string is : " + str(test_str))

# initializing K 
K = 'a'

cnt = 0
res = 0
for idx in range(len(test_str)):
	
	# increment counter on checking
	if test_str[idx] == K:
		cnt += 1
	else:
		cnt = 0
		
	# retaining max
	res = max(res, cnt)

# printing result 
print("The Longest Substring Length : " + str(res)) 
res = re.findall( K + '+', test_str)
print(res)

test_list = ["Gfg is good", "for Geeks", "I love Gfg", "Gfg is useful"]
K = "Gfg" 
for i, j in enumerate(test_list):
    if K in j:
        print(i,j) 

test_str = 'geeksforgeeks is best for geeks'
sub_str = 'for'
print(test_str[0:test_str.index(sub_str+" ")])
          
