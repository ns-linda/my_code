string="Hello from shu.bhamg199630@gmail.com to priya@yahoo.com about the meeting @2PM"
import re
pattern = r'\S+@\S+'
a=re.findall(pattern, string)
print(a)

color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]
print(set(color1) | set(color2))

listi= ["Yogesh", "is", "my", "love"]
n=3
print([i for i in listi if len(i)>3])

list_num=[1,2,3,4,5,6,7,8]
even =[i for i in list_num if i%2 ==0]
odd =[i for i in list_num if i%2 !=0]
print(even)
print(odd)
list = [5, 1, -96, -4, 2, 3, -1, -8, 9]
for i in range(len(list)-1):
    for j in range(len(list)):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]
print(list)
import re
str = "d 10.116.1.216 sfd 2.2.2.3 sdfsdf"
pattern = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
a= re.findall(pattern, str)
print(a)
pattern2 = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
a= re.findall(pattern2, str)
print(a)

pat=re.compile(r"25[0-5]|2[0-4]")
