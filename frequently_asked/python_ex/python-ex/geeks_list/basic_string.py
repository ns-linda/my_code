test ='khokho'
a= len(test) // 2
if test[a:] == test[:a]:
    print("symmetrical")
if sorted(test) != test:
    print("The entered string is not palindrome")

str ="geeks quiz practice code"
print(" ".join(i for i in str.split(" ")[::-1]))

Input= 'Geeks123For123Geeks'
pattern = '\D'
import re
word = re.findall(pattern, Input)
print("".join(word))
s = "This is a python language"
print(" ".join(j for i,j in enumerate(s.split(" ")) if len(j)%2 ==0))
for i ,j in enumerate(s.split()):
    print(i,j)
test_str = 'geeksforgeek' 
a = len(test_str)//2
print("".join(test_str[:a]+test_str[a:].upper()))
a = "hello world"
s=''
print((a[0].capitalize()+a[1:len(a)-1]+a[-1].capitalize()))
s += a[0].capitalize()+a[1:len(a)-1]+a[-1].capitalize()
print(s)
a = 'welcome2ourcountry34'
pattern = r'[a-zA-Z]+[0-9]+'
res = re.findall(pattern, a)
print(res)

vowels = 'aeiou'
s = "ABeeIghiObhkUul"
pattern = r'[a|e|i|o|u|A|E|I|O|U]'
k = re.findall(pattern, s)
print(k)
n={}
d = {i for i in vowels if i in s.lower()}
if len(d) == len(vowels):
    print(True)

str1 = 'aabcddekll12@'
str2 = 'bb22ll@55k'
n={}
for i in str1:
    if i in str2:
        n[i]=True
print(n)

a='geeksforgeeks'
print("".join(dict.fromkeys(a))) 

a='GeeksforGeeks'
n={}
for i in a:
    if i not in n:
        n[i]= 1
    else:
        n[i]+=1
print(n)
print(min(n, key = n.get))
print(max(n, key = n.get))
print([i for i,j in n.items() if j%2 !=0])

test_list = ["geeksforgeeks is best for geeks"]
chr_list = ["e", "b", "g", "f"] 
print({i:j.count(i) for i in chr_list for j in test_list if i in j})

test_str = "geeks4feeks is No. 1 4 geeks"
pattern = '[0-9]'
res= re.findall(pattern, test_str)
print(len(res))
test_str='Geeks$For$Geeks'

print([i for i in test_str if  not i.isalpha() or  not i.isalnum()])
str = "hello geeks for geeks is computer science portal" 
k = 4
print([i for i in str if len(i)>k])

f ='Geek'
a=list(f)
i = 1
a.pop(i)
print("".join(a))
test= ['Geeks', 'for', 'Geeks']
print("-".join(test))

sampleInput = "1001010ges"
pattern = r'[a-z][2-9][A-Z]'
res = re.findall(pattern,sampleInput)
print(res)

import re

patterns = ['ape', 'apple', 'peach', 'puppy']
input_str = 'appel'
# pattern = r'a|p|p|e|l'
pattern = '|'.join(input_str)
print(pattern)

res = {i: "".join(re.findall(pattern, i)) for i in patterns}
print(res)
print({i for i, j in res.items() if len(i)==len(j)})

A = 'Geeks for Geeks'
B = 'Learning from Geeks for Geeks'
# Output : [‘Learning’, ‘from’]
 
print (list(set(B.split()) - set(A.split())))

A = 'apple banana mango'
B = 'banana fruits mango'

l=list(set(B.split()) - set(A.split()))
m = list(set(A.split()) - set(B.split()))
print(l+m)
a=[]
b=[]
for i in A.split():
    if i not in B.split():
        a.append(i)
for i in B.split():
    if i not in A.split():
        b.append(i)
print(a+b)

import re

# Example JSON data
json_data = [{'id': 'd724f231-a9a7-b897-57c4-394d6622bc47', 'name': 'mgmt', 'ip': '10.67.9.19/24', 'operationalState': 'OPERATIONAL', 'modelName': 'D1048', 'modelVersion': '', 'manufacturerModelName': 'AS4630-54TE', 'manufacturerModelVersion': 'R01F', 'hardwareId': '03000200-0400-0500-0006-000700080009', 'systemSerialNumber': 'SV4423HFS00007', 'ports': [{'name': 'Ethernet0', 'operationalState': 'OPERATIONAL', 'physicalSlot': '1', 'speed': '1000M', 'mtu': 1500}]}]

# Function to check if the 'physicalSlot' is a numeric value
def check_physical_slot(json_data):
    try:
        # Assuming there is only one port in the 'ports' list for simplicity
        port = json_data[0]['ports'][0]
        physical_slot = port.get('physicalSlot')

        if physical_slot is not None and re.match(r'^\d+$', physical_slot):
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
if check_physical_slot(json_data):
    print("Physical Slot is a numeric value.")
else:
    print("Physical Slot is not a numeric value or not present.")

import re

pattern =  r'^myriad://[a-zA-Z0-9.-:]+/[a-zA-Z0-9-]+/nvme\d+$'

url = "myriad://10.65.179.247:7500/5af74407-667b-90c9-000c-2962664ca087/nvme6"

if re.match(pattern, url):
    print("The URL matches the pattern.")
else:
    print("The URL does not match the pattern.")

p = "14, 625, 498.002"
p = p.split(", ")
s  = [i.replace(".", ",") if "." in i else i for i in p ]
print(".".join(s))

txt = "14, 625, 498.002"
x = re.sub(', ', 'sub', txt)
x = re.sub('\.', ', ', x)
x = re.sub('sub', '.', x)
print(x)

#####################permutations#######
def perm(str):
    if len(str) ==1:
        return [str]
    final_list = []
    for i in range(len(str)):
        f = str[i]
        res = str[:i] + str[i+1:]
        for i in perm(res):
            final_list.append(f+i)
    return final_list
str = 'ABC'

print(perm(str))

string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'
pattern =  r'https://[a-zA-Z0-9./+\?%]+'
res = re.findall(pattern, string)
print(res)

f= string.split()
for i in f:
    if i.startswith("https://"):
        print(i)

test_str = 'geeksforgeeks'
k = 'sees'
inp = {i:j for i, j in enumerate(k)}
res = {i:j for i,j in enumerate(test_str) if j in inp.values()}
print(inp)
print(res)
val="".join(res.values())
print(val) 
if k in val:
    print("yes")
else:
    print("no")
res= ''
for i in test_str:
    if i in k:
        res +=i
print(res)
if k in res:
    print("yes")

for i in test_str:
    if i not in k:
        test_str=test_str.replace(i,"")
print(test_str)
if k in res:
    print("yes")
else:
    print("no")

s ="GeeksforGeeks is best for geeks"
split = "best"
res= s.split("best")
print("".join(res[0]))


