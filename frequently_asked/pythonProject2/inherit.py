class person:

    def __init__(self, name, empid):
        self.name = name
        self.empid = empid

    def show(self):
        print("Name is  {} and Emp id is {}".format(self.name, self.empid))

class person2(person):

    def __init__(self, name, empid, salary):
        self.salary = salary
        # person.__init__(self,name, empid)
        super().__init__(name, empid)

    def show_1(self):
        print("Name is  {} , Emp id is {} and salary is {}".format(self.name, self.empid, self.salary))

obj = person2('Linda', 10, 3000)
obj.show()
obj.show_1()









# def square(n):
#     num=0
#     for i in range(1,n+1):
#         num = num+ (i*i)
#     print(num)
#
# square(4)