# class singleton:
#
#     __shared_state = dict()
#     print(__shared_state)
#
#     def __init__(self):
#         self.__dict__ = self.__shared_state
#         print(self.__dict__)
#         self.state = 'Linda'
#
#     def __str__(self):
#         return self.state
#
# obj1=singleton()
# obj2=singleton()
# obj1.state = "Dani"
# obj2.state = "Abi"
#
# print(obj1)
# print(obj2)

class Singleton:
   __instance = None
   @staticmethod
   def getInstance():
      """ Static access method. """
      if Singleton.__instance == None:
         Singleton()
      return Singleton.__instance
   def __init__(self):
      """ Virtually private constructor. """
      if Singleton.__instance == None:

         Singleton.__instance = self
s = Singleton()
print(s)

s = Singleton.getInstance()
print(s)

s = Singleton.getInstance()
print(s)


class Singleton(object):

   def __new__(cls, *args, **kwargs):
      if not hasattr(cls, 'instance') or not cls.instance:
         cls.instance = super().__new__(cls)
      return cls.instance

   def __init__(self, language):
      self.language = language


obj1 = Singleton("English")
obj2 = Singleton("German")

print(obj1)
print(obj2)
# will print the same instance

print(obj1 == obj2)