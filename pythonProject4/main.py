class person:
    planet = 'earth'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name, self.age)

    def show(self):
        print(self.name, self.age)

    @classmethod
    def info(cls):
        print("The person belongs to planet", cls.planet)

    @staticmethod
    def find_age(age):
        if age > 31:
            print("adult")
        else:
            print("not an adult")

obj = person("linda", 32)
obj.show()
person.info()
person.find_age(32)

###inhetitance
class student:

    def __init__(self):
        self.name = "linda"
        print(self.name)

    def show(self):
        print("dept: pcmb")

class student1(student):

    def __init__(self):
        super().__init__()
        print("vijay")

    def show2(self):
        print("dept: pcme"
              )

obj=student1()
obj.show()
obj.show2()

###polymorphism
def concat(dt,*args):
    if dt == int:
        ans = 0

    else:
        ans =''
    for i in args:
        ans = ans+ i
    return ans

print(concat(int,5,4))
print(concat(str, 'linda', 'catherine'))

##private and protected

class A:
    def __init__(self):
        self.a = 3
        self._b = 4
        self.__c = 3

class B(A):

    def __init__(self):
        super().__init__()
        self._b =3
        print(self.a,self._b) #self.__c)
ob=A()
obj = B()
print(obj.a)
print(obj._b)
print(ob._b)

from abc import ABC, abstractmethod
class A(ABC):

    @abstractmethod
    def show(self):
        pass

class B(A):

    def show(self):
        print("äbstract method is implemented here")

obj = B()
obj.show()




