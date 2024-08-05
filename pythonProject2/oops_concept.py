class car():

    def __init__(self, model,color):
        self.model=model
        self.color=color

    def show(self):
        print("model", self.model)
        print("color", self.color)

audi = car("audi", "black")
# audi.show()

class dog():
    def __init__(self):
        print("dog is an animal")
    def bark(self):
        print("dog can bark")
        self.b=3
        self.__a=16
class dog2(dog):
    def eat(self):
        print("dog can eat")
        print(self.b)
        # print(self.__a)
class dog3(dog):
    def __init__(self):
        super().__init__()

obj=dog2()
ob2=dog3()
obj.bark()
obj.eat()


class car():

    # init method or constructor
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show(self):
        print("Model is", self.model)
        print("color is", self.color)


# both objects have different self which
# contain their attributes
audi = car("audi a4", "blue")
ferrari = car("ferrari 488", "green")

# audi.show()  # same output as car.show(audi)
# ferrari.show()  # same output as car.show(ferrari)
#########method overriding###
def data_type(dp, *args):
    answer =''
    if dp == str:
        answer = ''
    elif dp == int:
        answer = 0
    for i in args:
        answer = answer + i

    print(answer)


data_type(str,'hi','lida')
data_type(int,3,4)


class A:

    def fun1(self):
        print('feature_1 of class A')

    def fun2(self):
        print('feature_2 of class A')


class B(A):

    # Modified function that is
    # already exist in class A
    def fun1(self):
        print('Modified feature_1 of class A by class B')

    def fun3(self):
        print('feature_3 of class B')


# Create instance
obj = B()

# Call the override function
obj.fun1()

###private and protected
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"


# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)

# Uncommenting print(obj1.c) will
# raise an AttributeError

# Uncommenting obj2 = Derived() will
# also raise an AtrributeError as
# private member of base class
#
class MyClass:
    # Hidden member of MyClass
    __hiddenVariable = 10


# Driver code
myObject = MyClass()
print("hidden")
print(myObject._MyClass__hiddenVariable)


class Base(object):
    pass  # Empty Class


class Derived(Base):
    pass  # Empty Class


# Driver Code
print(issubclass(Derived, Base))
print(issubclass(Base, Derived))

d = Derived()
b = Base()

# b is not an instance of Derived
print(isinstance(b, Derived))

# But d is an instance of Base
print(isinstance(d, Base))

####### static and class method #######
class person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def birthyear(cls,name, age):
        return (2021 - age)

    @staticmethod
    def isadult(age):
        if age >30:
            return True

person1=person("linda",30)
person2=person.birthyear("danita",25)
print(person1.name, person1.age)
print(person2)
print(person.isadult(31))
