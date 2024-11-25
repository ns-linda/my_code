from abc import ABC, abstractmethod

class a:

    @abstractmethod
    def method1(self,name):
        ...


class b(ABC):
    def method1(self,name):
        print("abstarct method")

obj = b()
obj.method1("linda")

from abc import ABCMeta, abstractmethod


class A(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def method1(self, name):
        ...

    def method2(self):
        print("method2")

class B(A):

    def method3(self):
        self.method2()

    def method1(self, name):
        print("abstract method1")

b = B()
b.method3()
b.method1("yogesh")

from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def abs(self):
        pass

class B(A):
    def abs(self):
        print("this is derived from abstarct class")

obj=B()
obj.abs()