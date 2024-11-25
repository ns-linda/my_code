# Define input string
test_str = 'void'
 
# Define mirror dictionary
mir_dict = {'b': 'd', 'd': 'b', 'i': 'i', 'o': 'o', 'v': 'v', 'w': 'w', 'x': 'x'}
res=''
for ele in test_str:
    if ele in mir_dict:
        res += mir_dict[ele]
print(res)


test_str = 'geeksforgeeks is best'
map_dict = {'e':'1', 'b':'6'} 
print("".join([map_dict[i] if i in map_dict else i for i in test_str ]))

test_str = 'geeksforgeeks is best'
 
# printing original string 
print("The original string is : " + test_str) 
test_str =list(test_str)
# initializing list 
test_list = [2, 4, 7, 10] 
for i,j in enumerate(test_str):
    if i in test_list:
        test_str[i]='*'
print("".join(test_str))

print("".join(["*" if i in test_list else i for i in test_str]))

# The original list is : ['gfg', '   ', ' ', 'is', '            ', 'best']
# List after filtering non-empty strings : ['gfg', 'is', 'best']
inp = ['gfg', '   ', ' ', 'is', '            ', 'best']
print([i for i in inp if not i.isspace()])

inp = 'Gfg, is best: for ! Geeks ;'
import re
from turtle import position
res = re.sub('[^\w\s]', '', inp)
print(res)
import string
for pun in string.punctuation:
    inp = inp.replace(pun, "")
print(inp)
test_str1 = 'e!e!k!s!g'
test_str2 = 'g!e!e!k!s'
delim = '!'
if sorted(test_str1.split(delim)) == sorted(test_str2.split(delim)):
    print("yes")

# Input : test_str = ‘geeksforfreeksfo’, K = 3
# Output : geeksforfree
test_str = 'geeksforfreeksfo'
k=3
test_str = 'geeksforfreeksfo'
  
# printing original string 
print("The original string is : " + str(test_str)) 
  
# initializing K  
K = 3
  
memo = set() 
res = [] 
for idx in range(0, len(test_str) - K): 
      
    # slicing K length substrings 
    sub = test_str[idx : idx + K] 
      
    # checking for presence 
    if sub not in memo: 
        memo.add(sub) 
        res.append(sub) 
print(memo)
print(res)
for ele in range(0, len(res), 3):
    print(res[ele])

word = ['allx', 'lovex', 'gfg', 'xit', 'is', 'bestx']
print([i for i in word if  not i.endswith('x')])

a=  'hello'
n={}
# print("".join((dict.fromkeys(a))))
for i in a:
    if i in n:
        n[i] +=1
    else:
        n[i] =1
print([i for i, j in n.items() if j > 1])

string="Gfg is best . Gfg also has Classes now. Classes help understand better "
repl_dict = {'Gfg' : 'It', 'Classes' : 'They' } 
ns=[]
for i in string.split(" "):
    if i not in ns:
        ns.append(i)
    elif i in ns and i in repl_dict.keys():
        # ns.append(repl_dict[i])
        i = repl_dict[i]
        ns.append(i)
print(" ".join(ns))

str = " Jan = January; Feb = February; Mar = March"
str1 = str.split(";")
print(str1)
nw={}
print(dict(s.split("=") for s in str.split(";")))
for i in str1:
    i = i.split("=")
    nw[i[0]]=i[1]
print(nw)

str1 = "Jan, Feb, March"
str2 = "January | February | March"
str1 = str1.split(",")
str2 = str2.split("|")
print(dict(zip(str1, str2)))

from datetime import datetime

end_time = "2023-11-09_06.40.46.994887"
start_time = "2023-11-09_04.57.21.832461"

# Convert timestamps to datetime objects
end_datetime = datetime.strptime(end_time, "%Y-%m-%d_%H.%M.%S.%f")
start_datetime = datetime.strptime(start_time, "%Y-%m-%d_%H.%M.%S.%f")

# Calculate the time difference in seconds
time_difference = (end_datetime - start_datetime).total_seconds()

print("Time taken (seconds):", time_difference)

    