import pickle

f= open("txt.txt",'ab')
val=10
pickle.dump( int(val),f)

f =open("txt.txt",'r')
# value = pickle.load(f)

# print(value)

import json
python_dict = {
    "username": "jiangnanmax",
    "age": 21
}

print(json.dumps(python_dict))

with open("ex_jso.json","w") as file:
    file.write(json.dumps(python_dict))

import os
print(os.stat("txt.txt").st_size)

import xml.dom.minidom as xml

import xml.dom.minidom as xml

parse = xml.parse("xml file path")

print(parse.nodeName)
print(parse.getElementsByTagName("html"))   
