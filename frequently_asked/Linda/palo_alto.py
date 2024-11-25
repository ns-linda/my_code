def print_pairs(arr, n):
    d={}
    for i in range(0,len(arr)):
        val = n-arr[i]
        print(val)
        if val in d:
            print(arr[i], val)
        d[arr[i]]=val
    # print(d)
arr = [1, 2, 40, 3, 9, 4,0]
N = 3
print_pairs(arr, N)

#The idea is to use collections and pprint module as shown below:

import collections
import pprint
with open("2.txt", 'r') as data:
 count_data = collections.Counter(data.read().upper())
 count_value = pprint.pformat(count_data)
print(count_value)

def add_nums(num1, num2):
   while num2 != 0:
       data = num1 & num2
       print(data)
       num1 = num1 ^ num2
       print(num1)
       num2 = data << 1
   return num1
print(add_nums(2,10))
import re
def match_text(txt_data):
       pattern = 'ab{4,8}'
       if re.findall(pattern,  txt_data):    #search for pattern in txt_data
           return 'Match found'
       else:
           return('Match not found')
print(match_text("abc"))         #prints Match not found
print(match_text("aabbbbbc"))

d1 = {'key1': 50, 'key2': 100, 'key3':200}
d2 = {'key1': 200, 'key2': 100, 'key4':300}
print({key : d1.get(key,0)+d2.get(key,0) for key in (set(d1)| set(d2))})


