# input: S = “zero four zero one”
# Output: 0401
from cgi import test
import enum


s= "zero four zero one"
convert_number = {1: "one",
                  2: "two",
                  3: "three",
                  4: "four",
                  0: "zero"}
print("".join(str(x) for i in s.split(" ") for x, y in convert_number.items()  if i ==y))

# The original string is : geeksforgeeks is best for geeks
wrd = 'best'
s = "geeksforgeeks is best for geeks"
print([i+1 for i,j in enumerate(s.split(" ")) if j ==wrd])


from itertools import groupby
s="geekksforgggeeks"
# The Consecutive characters frequency : [1, 2, 2, 1, 1, 1, 1, 3, 2, 1, 1]
print({i:s.count(i) for i in s})
# for _, j in groupby(s):
#     print(_,list(j))

# initializing string
test_str = "geekksforgggeeks"

# printing original string
print("The original string is : " + test_str)

# Consecutive characters frequency using loop
res = []
count = 1
for i in range(len(test_str)-1):
	# print(test_str[i], test_str[i+1])
	if test_str[i] == test_str[i+1]:
		count += 1
	else:
		res.append(count)
		count = 1
	# print(count)
res.append(count)

# printing result
print("The Consecutive characters frequency : " + str(res))

# Input : s = "GeeksforGeeks"
#         d = 2
# Output : Left Rotation  : "eksforGeeksGe" 
#          Right Rotation : "ksGeeksforGee"
s="GeeksforGeeks"
d=2
print(s[-2:])
print("".join(s[2:]+s[0:2]))
print("".join(s[-d:] + s[0:len(s)-d]))
import re
str = "GEEGEEKSKS"
sub_str = "GEEKS"
import re

str = "GEEGEEKSKS"
sub_str = "GEEKS"

while len(str) != 0:
    match = re.search(sub_str, str)
    if match:
        str = re.sub(sub_str, "", str, count=1)
print(str)

# Input : eeksg, geeks
# Output: 1
s= "eeksg"
print(s[2:]+s[0:2])
actual = "geeks"
for i in range(len(s)):
	print("".join(s[i+1:]+s[0:i+1]))
	if "".join(s[i+1:]+s[0:i+1])== actual:
		print(i, s[i])

x=0
str2 = "sgeek"
m=s
while True:
         
        # left rotating the string
        m = m[len(m)-1] + m[:len(m)-1] 
         
        # checking if rotated and 
        # actual string are equal.
        if(m == str2):
            x += 1
            break
             
        else:
            x += 1
            if x > len(str2) :
                break
print(x)

# Input : test_str = 'geeks are for geeksforgeeks', que_word = "geek" 
# Output : {'s': 3} 
test_str = 'geeks are for geeksforgeeks'
que_word = "geek" 
n={}
for i in range(len(test_str)-1):
    print(test_str[i:i+len(que_word)])
    if test_str[i:i+len(que_word)] == que_word:
          char=test_str[i+len(que_word)]
        #   print(char)

## Rotationally equivalent
test_str1 = 'GFG'
test_str2 = 'FGG'
x=0
while True:
      print(test_str2[x:]+test_str2[:x])
      if test_str2[x:]+test_str2[:x] == test_str1:
            print(x)
            break
      else:
            x +=1
            if x > len(test_str2):
                  break

res=False
for i in range(len(test_str1)):
      if test_str2[i:]+test_str2[:i] == test_str1:
            res = True
            break
print(i)
print(res)

test_str1 = "geeksforgeeks"
test_str2 = "gfks"
print(all(ele in test_str1 for ele in test_str2))

test_list1 = ["Gfg", "is", "best"]
test_list2 = ["I love Gfg", "Its Best for Geeks", "Gfg means CS"] 

t = any(any(word in i.split() for word in test_list1) for i in test_list2)
print(t)

            
      
	

