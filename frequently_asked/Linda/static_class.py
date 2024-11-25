# class Myclass:
#
#     name = "Yogesh"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def method(self):
#         self.age = 20
#         return 'instance',self
#
#     @classmethod
#     def classmethod(cls):
#         return cls.name
#
#     @staticmethod
#     def staticmethod():
#         return 'static'
#
# obj = Myclass("linda", 31)
# print(obj.method())
# print(obj.age)
# print(Myclass.classmethod())
# print(Myclass.staticmethod())

class Example:
    var =1
    def __init__(self,name):
        self.name = name

    def area(self):
        self.vari=30

    @staticmethod
    def square():
        var2 =20

    @classmethod
    def check_var(cls):
        cls.var=2

obj = Example("linda")
obj.area()
print(obj.vari)
# print(Example.var2)
print(Example.var)
