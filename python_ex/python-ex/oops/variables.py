class test:
    class_variable= 1 #class variable or static variable

    def __init__(self,name):
        self.name  = name
        test.class_variable +=1
        print(self.name)

obj = test("object1")
print(obj.name)
print(test.class_variable)

###### class , static method, instance method

class person(test):
    age=28
    def __init__(self, m1):
        super().__init__("linda")
        self.m1 = m1


    @classmethod
    def info(cls):
        cls.age=20
        return cls.age
    
    @staticmethod
    def isadult(age):
        if age<30:
            return False
obj1=person(28)
print(person.age)
print(obj1.info())
print(obj1.isadult(2))