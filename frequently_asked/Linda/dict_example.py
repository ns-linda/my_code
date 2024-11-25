class Vehicle:
    kind = "car"
    def __init__(self, name, model):
         self.name = name
         self.model = model

def from_dict(dict):
        instance = Vehicle("None", "None")
        instance.__dict__.update(dict)
        return instance


car = Vehicle("abc", "xyz")
print(car.__dict__)
class_state = car.__dict__.copy()
del car
car = Vehicle("sfd", "sfd")
car.__dict__.update()
print(car.__dict__)

del car
car = from_dict(class_state)
print(car.__dict__)

name = "linda"
print(f"my name is {name}")

dict = {'a': 1, 'e': 4, 'c': 3, 'd': 5, 'b':2 }
value = sorted(dict.values())
nw={}
nw_value={}
for i,j in sorted(dict.items()):
    nw[i]=j
print(nw)

for i in value:
    for j in dict.keys():
        if i == dict[j]:
            nw_value[j] = i
print(nw_value)


