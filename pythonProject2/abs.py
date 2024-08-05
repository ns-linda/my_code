from abc import ABC, abstractmethod
class emp(ABC):

    @abstractmethod
    def view(self):
        print("in abs")

class office(emp):
    def view(self):
        print("method from abstract")

obj = office()
obj.view()

