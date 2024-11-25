class example:

    var=100
    def __init__(self):
        self.var1 = 200

    def instance(self):
        self.var2=300

    @staticmethod
    def show():
        var3=400
        return var3

    @classmethod
    def show_cls(cls):
        cls.var4 = 500
        return cls.var4

e=example()
print(e.var)
print(e.var1)
e.instance()
print(e.var2)
print(example.show())
print(example.show_cls())
# print(example.var4)

