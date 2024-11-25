from random import sample


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
d={}
for i in range(len(keys)):
    # for j in range(len(values)):
    #     d[keys[i]]=values[i]
        d.update({keys[i]:values[i]})
print(d)
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3=dict1.copy()
dict3.update(dict2)
print(dict3)

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
for i, j in sampleDict.items():
    for k,l in j.items():
        print(l['marks']['history'])
print("$$$$$$$$$$$$$$$$")
print(sampleDict['class']['student']['marks']['history'])

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
o={'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
v={}
for i in employees:
    v[i]=defaults
print(v)

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
n={}
for i in keys:
    n[i]=sample_dict[i]
print(n)
new={i: sample_dict[i] for i in keys}
print(new)

## delete == pop
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
res = min(i for i,j in sample_dict.items())
print(res)
res1=min(sample_dict, key = sample_dict.get)
print(res1)
print(min(sample_dict, key = lambda x:sample_dict[x]))
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
print(sample_dict['emp3']['salary'])