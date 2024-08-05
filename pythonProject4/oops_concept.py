class person:
    planet = "earth"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def view(self):
        print("The name is", self.name ,"and age is", self.age)

    @classmethod
    def birthyear(cls, name, age):
        print("name is", name, "and age is", (age), cls.planet)

    @staticmethod
    def check_age(age):
        if age > 31:
            print("adult")
        else:
            print("Not an adult")

if __name__ == "__main__":
    obj1 = person("vijay", 32)
    obj1.view()
    person.birthyear("linda",31)
    person.check_age(32)
    print(obj1.planet)


######inheritance

class student:

    def __init__(self):
        print("student of 2021")

    def dept(self):
        print("PCMB")

    def show(self):
        print("This is from super class")

class student1(student):
    def __init__(self):
        super().__init__()

    def dept(self):
        print("commerce")


ob1 = student1()
ob1.dept()
ob1.show()
ob2= student()
ob2.dept()

###polymorphism

def concat_var(dt, *args):

    if dt == str:
        dt =''

    if dt == int:
        dt = 0
    for i in args:
        dt = dt + i
    return dt

if __name__ == "__main__":
    print(concat_var(int,5,6))
    print(concat_var(str,"linda","catherine"))

######private and protected

class person:

    def __init__(self, name, age, height):
        self.name = name
        self._age = age
        self.__height = height
        print(self.name, self._age, self.__height)

class person2(person):

    def __init__(self, name, age, height):
        super().__init__(name, age, height)

    def display(self):
        print(self.name)
        self._age = 50 ### protected can be modified as well
        print(self._age)
        # print(self.__height)


#Protected: The members of a class that are declared protected are only accessible to a class derived from it. underscore ‘_’ symbol
#private:The members of a class that are declared private are accessible within the class only,  underscore ‘__’ symbol



o = person("linda",32,5)
o.name = "christy"
o._age = 35
print(o.name, o._age)
o1 = person2("linda",32,5)
o1.display()

## Abstract

from abc import ABC, abstractmethod

class a(ABC):
    @abstractmethod
    def view(self):
        print("abstarct method")

class b(a):
    def view(self):
        print("from abstarct")

abs=b()
abs.view()


####workout
class Emp:
    company = "abc"
    def __init__(self, name, age):
        self.name= name
        self.age =age

    @staticmethod
    def check_age(age):
        if age > 31:
            print("adult")

    @classmethod
    def get_company(cls):
        if cls.company == "abc":
            cls.company="xyz"
        return cls.company
obj = Emp("linda", 32)
print(Emp.company)
obj.check_age(32)
obj.get_company()
print(Emp.company)

class A:
    def show(self):
        print("class A")
class B(A):
    def show(self):
        print("class B")
obj=B()
obj.show()

from abc import abstractmethod, ABC

class A(ABC):
    @abstractmethod
    def show(self):
        pass
class B(A):
    def show(self):
        print("asyart")
obj=B()
obj.show()






