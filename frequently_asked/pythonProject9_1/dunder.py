class Cal:
    def __init__(self, string):
        self.string = string
        print(self.string)
    def __del__(self):
        pass

    def __repr__(self):
        return ('object {}'.format(self.string))

    def __str__(self):
        return (self.string)

    def __add__(self, other):
        return (self.string + other)
obj=Cal("heloo")
print(dir(obj))
print(obj + " linda")
print(repr(obj))
# del obj