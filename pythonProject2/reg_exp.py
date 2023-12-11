import re
string = "Hello my Number is 123456789 and my friend's number is 987654321"
reg_ex = '\d+'
match = re.findall(reg_ex, string)
print(str(match))

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

y = re.split("9", x)
print(y)
