def left_rotation(str, n):
    char_list = list(str)
    char = char_list[n:] + char_list[:n]
    final = "".join(char)
    return final

def right_rotation(str, n):
    char_list = list(str)
    char = char_list[-n:] + char_list[:-n]
    final = "".join(char)
    return final

string = "geeksforgeeks"
n = 3
left = left_rotation(string,n)
right = right_rotation(string,n)
print("Original string:", string)
print("Left rotated string:", left)
print("Right rotated string:", right)
 
string_input = "eeksg"
sub_str = "geeks"
x = 0 
y=0
while True:
    s = str(string_input)
    # print(s[len(s)-1]+ s    [:len(s)-1])
    if s[len(s)-1]+ s[:len(s)-1]  == sub_str:
        x +=1
        break
    else:
        x +=1
        if x>len(s):
            break
while True:
    if s[1:len(s)]+s[0] == sub_str:
        y +=1
        break
    else:
        y +=1
        if y > len(s):
            break
print("left", x)
print("right", y)

test_str = 'geeks are for geeksforgeeks'
que_word = "geek"
d ={}
for i in range(len(test_str)-1):
    if test_str[i:i+len(que_word)]== que_word:
        char = test_str[i+len(que_word)]
        if char in d:
            d[char] +=1
        else:
            d[char] =1
print(d)

# Input : test_list = [“geekforgeekss”, “is”, “bessst”, “for”, “geeks”], K = ‘s’ 
# Output : [‘bessst’, ‘geekforgeekss’, ‘geeks’, ‘is’, ‘for’] 
test_list = ['geekforgeekss', 'is', 'bessst', 'for', 'geeks']
K = 's'
a= {i:i.count(K) for i in test_list}
print(a)
b = {i:j for y in sorted(a.values(), reverse=True) for i, j in a.items()  if y ==j}
print(b.keys())

test_list = ["geekforgeeks", "is", "best", "for", "geeks"]
 
# printing original list
print("The original list is : " + str(test_list))
 
# initializing K
K = 20

res = [ele[0] for sub in enumerate(test_list) for ele in enumerate(sub[1])]
print(res)
# getting index of word
res = res[K]
 
# printing result
print("Index of character at Kth position word : " + str(res))
test_str = "gfg, is, (best, for), geeks"
import re
l = re.split(r',(?![()])', test_str)
print(l)
test_str = 'GFGaBstuforigeeks'
pattern=r'[aeiou]'
l= re.split(pattern, test_str)
print(l)


        


