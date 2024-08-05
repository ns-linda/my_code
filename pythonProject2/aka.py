# s1= "abC%def&gykm"
#
# s2= "mky%gfe&dCba"
# j=''
# a=[]
# for i in s1:
#     if i.isupper() or i.islower():
#         j = str(i)+str(j)
# print(j)
# for i, k  in enumerate(s1):
#     if k is not k.isupper() or  k is not k.islower():
#         print(k)
#         list(j).insert(i,k)
#
# print(j)

class person:
    def __init__(self):
        print("Hi, am Linda")
        self.__a=3

    def eat(self):
        print("dog eats food")

class person_1(person):
    def __init__(self):
        super().__init__()

obj2=person_1()
obj2.eat()
# print(obj2.__a)

class person():
    def __init__(self,name,age):
        self.name= name
        self.age = age

    @classmethod
    def birthyear(cls,name,age):
        return(2022 - age)

    @staticmethod
    def isadult(age):
        if age>30:
            return True
        else:
            return False


obj=person("latha",50)
obj2=person.birthyear("linda",31)
obj3 = person.isadult(25)
print(obj)
print(obj2)
print(obj3)

###sorting
l1=[1, 2, 3]
l2=[9, 2, 1]
l3=l1+l2
l3.sort()

for i in range(len(l3)):
    min_idx = i
    for j in range(i+1,len(l3)):
        if l3[i] < l3[j]:
            min_idx = j

    l3[min_idx], l3[j] =  l3[j]  , l3[min_idx]

print(l3)
##reverse
l4=''
for i in l3:
    l4 = str(i)+ str(l4)


print([i.split(" ") for i in l4])# print(' '.join(l4))