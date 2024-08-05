import re
test_string = "There are 2 apples for 4 persons"
x = [' '.join(i) for i in test_string if re.findall("\d", i)]
print(x)
num=[]
for i in test_string:
    if i.isnumeric():
        num.append(i)

print(num)