from abc import ABC, abstractmethod


class f1(ABC):
    @abstractmethod
    def display(ABC):
        pass


class f2(f1):
    def display(self):
        print("using abstarct method")

obj=f2()
obj.display()
