# class A:
#     def __init__(self):
#         self.name = 'John'
#         self.age = 23
#
#     def getName(self):
#         return self.name
#
# class B:
#     def __init__(self):
#         self.name = 'Richard'
#         self.id = '32'
#
#     def getName(self):
#         return self.name
#
# class C(A, B):
#     # pass
#     def __init__(self):
#         A.__init__(self)
#         B.__init__(self)
#
#     def getName(self):
#         return self.name
#
# C1 = C()
# print(C1.getName())
# print(C1.name)

class A:

    def __init__(self):
        print("This is from class A")

    def show(self):
        print("show of class A")

class B(A):

    def __init__(self):
        super().__init__()

class C(B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)

    def show_c(self):
        self.show()

c=C()
c.show()
