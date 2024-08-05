import json

d=json.loads("""{"name":"linda"}""")
print(d)
with open("1.json", "w") as jsonfile:
    jsonfile.write(json.dumps(d))

f=open("1.json", "r")
e=json.load(f)
print(f.read())

f1=open("2.json", "w")
json.dump({"age":32}, f1)

import os, re
print(os.stat("1.csv").st_size)

str = "d 10.116.1.216 sfd 2.2.2.3 sdfsdf"
pattern = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
match = re.findall(pattern, str)
print(match)

def find_valid(s):
    if s.count(".") < 3:
        print("invaid ip")
    l= s.split(".")
    for ele in l:
        if int(ele)<0 or int(ele)>255 and  (ele[0]==0 and len(ele)!=1):
            print("invalid")
    else:
            print("valid")

find_valid("10.116.1.216")
find_valid("2.2.2.3")
str = "d 10.116.1.216 sfd 2.2.2.3 sdfsdf"
def find(ip):
    pattern = "\s((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])"
    # "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    if re.search(pattern, ip):
        return True
    str = "d 10.116.1.216 sfd 2.2.2.3 sdfsdf"
    match= re.findall(pattern, str)
    print(match)
print(find("10.116.1.216"))

string = "In 2020, the avg temperatures in bangalore were variying from 15-25.30. The humidity also increased from 50.5% to 70.24%."
pattern = re.findall("\d+\W?\d+\W?\d+", string)
print(pattern)

from copy import copy, deepcopy
l1=[1,2,3,4]

l2=copy(l1)
# l3=deepcopy(l1)
l2[1]=5
print(l2)
print(l1)
# print(l3)
# print(l1)
mystr= "I love my India"
print(" ".join([(i[::-1]) for i in mystr.split(" ")]))

for i in range(0,10,2):
    print(i, end=",")

