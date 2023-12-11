class parent:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("This is from parent class")

class child(parent):
    def __init__(self,name, age):
        parent.name = name
        self.age = age

        print("Name and age", parent.name, self.age)

    def display_details(self):
        self.show()


obj = child("Linda", 30)
obj.display_details()
