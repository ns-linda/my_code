import m

def f(self):
        print("this is second")

obj=m.Myclass()
obj.f()


import pickle
file = open("1.txt", "ab")
value=10
pickle.dump(value, file)

fi= open("1.txt", "rb")
v=pickle.load(fi)
print(v)

import json

# JSON string:
# Multi-line string
data = """{ 
    "Name": "Jennifer Smith", 
    "Contact Number": 7867567898, 
    "Email": "jen123@gmail.com", 
    "Hobbies":["Reading", "Sketching", "Horse Riding"] 
    }"""

# parse data:
res = json.loads(data)

# the result is a Python dictionary:
print(res)

sample= json.loads('{"name":"yogesh"}')
print(sample)
data=json.load(open("txt.json"))
print(data)

python_dict= {
    "name": "linda",
    "age": 32
}
with open("1.json", "w") as file:
        file.write(json.dumps(python_dict))

with open("2.json", "w") as files:
    json.dump(python_dict, files, indent=4)