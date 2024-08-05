class Student:
    school = 'abc'  # static varaible or class variable
    def __init__(self, m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 =m3

    #instance method
    #Accessors"fetch and Mutators: modify
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def info(cls):
        return cls.school

    @staticmethod
    def data():
        print("static")

s1 = Student(1,2,3)
s2 = Student(2,3,4)
s3=Student.info()
s4=Student.data()
print(s3)
#print(s4)