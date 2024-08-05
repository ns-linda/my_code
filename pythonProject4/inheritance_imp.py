##public private

class a:
    def __init__(self, emp_name, age):
        self._emp_name = emp_name
        self.__age = age

    def show(self):
        print(self._emp_name, self.__age)

obj=a("linda", 32)
obj.show()

class parent:
    def __init__(self,name):
        self.name = name

class child(parent):
    def __init__(self, name, age):
        # parent.name= name
        super().__init__(name)
        self.age =age

    def display(self):
        print(self.name, self.age)

obj1= child("linda",32)
obj1.display()

#####hierarchical
class a:
    def a_func(self):
        print("a")

class b(a):
    def b_func(self):
        print("b")

class c(b):
    def c_func(self):
        print("c")

obj1=b()
obj2=c()
obj1.a_func()
obj1.b_func()
obj2.a_func()
obj2.c_func()

###multiple
class p1:
    def p1_func(self):
        print("p1_func")

class p2:
    def p2_func(self):
        print("p2_func")

class child(p1,p2):
    def child_func(self):
        self.p1_func()
        self.p2_func()

ob= child()
ob.child_func()
ob.p1_func()

class parent:

    def func1(self):
        print("func1")

class child(parent):
    def get_func(self):
        self.func1()

ob= child()
ob.get_func()

class Employee:
    place = "Bangalore"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_place(cls, name):
        print(cls.place, name)

    @staticmethod
    def check_age(age):
        if age > 31:
            print("adult")

obj = Employee("linda", 31)
Employee.get_place("classlinda")
Employee.check_age(32)


