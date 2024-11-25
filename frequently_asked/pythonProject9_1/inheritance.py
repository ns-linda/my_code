class a1:
    def __init__(self,a):
        self.a= a
        print(self.a)

class b1(a1):
    def __init__(self,a,b):
        self.b = b
        a1.__init__(self,a)
        print(self.a, self.b)

class c1(b1):
    def __init__(self,a,b,c):
        self.c=c
        b1.__init__(self,a,b)
        print(self.c, self.b, self.a)

obj = c1("linda","vijay", "kristine")
print(obj.c)

class feature1(object):
    def __init__(self, name1):
        self.name1= name1

class feature2(feature1):


    def __init__(self, name1, name2):
        self.name2= name2
        feature1.__init__(self,name1)

    def show(self):
        print("this is from feature2")

class feature3(feature2):
    def __init__(self, name1,name2, name3):
        self.name3= name3
        feature2.name2=name2
        feature2.__init__(self, name1,name2)

    def child_fn(self):
        self.show()
        print(feature2.name2)

obj1=feature3("kelly", "sherly", "anita")
print(obj1.name3)
obj1.child_fn()
obj1.show()


class Parent(object):
    # Constructor
    def __init__(self, name):
        self.name = name


class Child(Parent):
    # Constructor
    def __init__(self, name, age):
        Parent.name = name
        self.age = age

    def display(self):
        print(Parent.name, self.age)


# Driver Code
obj = Child("Interviewbit", 6)
obj.display()


class InterviewbitEmployee:
    # protected members
    _emp_name = None
    _age = None

    # private members
    __branch = None

    # constructor
    def __init__(self, emp_name, age, branch):
        self._emp_name = emp_name
        self._age = age
        self.__branch = branch

    # public member
    def display(self):
        print(self._emp_name + " " + str(self._age) + " " + self.__branch)

ob2 = InterviewbitEmployee("linda",32,"cse")
ob2.display()

import random
print(random.randrange(5,100,2))

print("#################")
class feature1:
    def __init__(self,a):
        self.a=a
class feature2(feature1):
    def __init__(self,a,b):
        feature1.__init__(self,a)
        self.b=b
        feature1.a = a

    def show(self):
        print(feature1.a)
        print(self.a)

obj = feature2(2,3)
obj.show()


