##method overriding

class bird():

    def __init__(self):
        print("Am a bird")

    def fly(self):
        print("I can fly")

class sparrow(bird):

    def fly(self):
        print("sparrow can fly")

obj= sparrow()
obj.fly()

#Method overloading

def datatype(type, *args):
    global answer
    if type == "int":
         answer = 0

    if type == "str":
        answer =''

    for x in args:
        answer = answer + x
    print(answer)

datatype("int", 2, 3)
datatype("str", 'wel', 'come')


