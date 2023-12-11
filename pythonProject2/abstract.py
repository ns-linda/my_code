from abc import ABC, abstractmethod
class f1(ABC):
    @abstractmethod
    def display(self):
        pass

class f2(f1):
    def display(self):
        print("using abc")

obj = f2()
obj.display()











from abc import ABC, abstractmethod

class person(ABC):

    @abstractmethod
    def view(self):
        pass

class person_1(person):
    def view(self):
        print("This is person1 method")

if __name__ == "__main__":
    obj = person_1()
    obj.view()

from abc import ABC, abstractmethod

class f1(ABC):
    @abstractmethod
    def p_print(self):
        pass

class f2(f1):
    def p_print(self):
        print("using ABC")

ob=f2()
ob.p_print()

