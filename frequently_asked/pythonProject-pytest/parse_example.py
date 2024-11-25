import json
import requests

name = {
    "name": ['linda', 'catherine'],
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
# print(name["email"])
# print(name["name"][0])

with open("data_ex.json", 'w') as file:
    file.write(json.dumps(name))

Tickets = {'12345' : {'SEV' : 1, 'Priority' : 'Mid'},
'12346' : {'SEV' : 2, 'Priority' : 'High'},
'12224' : {'SEV' : 1, 'Priority' : 'High'}}
for i in Tickets.keys():
    if(Tickets[i]['SEV']) == 1 and (Tickets[i]['Priority'])== "High":
        print(i)

for i, j in Tickets.items():
    if j["Priority"] == "High" and j['SEV']  ==1:
        print(i)


