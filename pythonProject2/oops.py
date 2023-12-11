## class, object, self, init, class method and static method
class person():

    def __init__(self,name, age):
        self.name = name
        self.age = age

    def view(self):
        print("My name is {} and my age is {}".format(self.name, int(self.age)))

    @classmethod
    def birthyear(cls,name, age):
        return(2021-age)

    @staticmethod
    def check_age(arg1):
        if arg1 < 30:
            return True



if __name__ == '__main__()':
    obj= person("Linda", 25)
    obj.view()
    obj2=person.birthyear("Danita", 25)
    print(obj2)
    obj3=person.check_age(25)
    print(obj3)