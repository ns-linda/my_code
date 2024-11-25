class Shark:
    animal = "sea"
    area = None
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_area(self):
        self.area = 14
        return self.area

    def set_followers(self, followers):
        # from locale import str
        print("This user has " + str(followers) + " followers")

shark = Shark("linda", 31)
print(Shark.animal)
shark1 = Shark("linda", 31)
shark1.animal = "land"
print(shark1.animal)
print(shark.animal)

print(shark.name)
print(shark.age)
print(shark.set_area())
shark.set_followers(17)
print(shark.area)