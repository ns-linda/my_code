animaldict = {
    "name": "Dog",
    "age": 5,
    "Weight": 4,
    "Country": "US",
    "City": "California"

}
d={key: animaldict[key] for key in ["name","age"]}

animaldict = {
    "name": "Dog",
    "age": 5,
    "Weight": 4,
    "Country": "US",
    "City": "California"

}

animaldict['Animalname'] = animaldict.pop('name')
fruitsDict = {
    'Apple': 100,
    'Orange': 200,
    'Banana': 400,
    'pomegranate': 600
}
print(min(fruitsDict , key = fruitsDict.get))

Fruit = {'Apple': 100, 'banana': 5}

Subject = {'Math': 100, 'English': 98}

animal = {'name': 'Rabbit', 'age': 1}
print(dict(zip(Fruit,Subject)))

a = Fruit.update(Subject)
b=Fruit.update(animal)
print(Fruit)
FruitDict = {'Apple': 600, 'Banana': 515,'Orange':214,'Guava':1116}
z=([i for i in sorted(FruitDict.values())])
print(z)
print(z[-2:])
import re
myDict = {'Fr   uit':['Apple','Banana','Orange'],'Sub    ject':['Phy','Math','English']}
dict={}
for key, value in myDict.items():
    s=key.replace(" ","")
    print(s)
    # d=re.compile(r'\s+')
    # f=re.sub(d,"",key)
    # if d:
    #     print(f)

c='Let us Learn Python'
upper={}
lower={}
uppercount=0
lowercount=0
for i in c:
    if i.isupper():
        upper[i] = uppercount+1
    if i.islower():
        lower[i] = lowercount+1
print(upper)
print(lower)
for i in c:
    if i.isupper():
        uppercount=uppercount+1
    if i.islower():
         lowercount = lowercount + 1
print(uppercount)
print(lowercount)

from collections import Counter

