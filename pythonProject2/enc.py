class base:

    def __init__(self):
        self.a = 1
        self._b =2
        self.__c =3

class dervied(base):

    def __init__(self):
        base.__init__(self)
        print(self.a)
        self._b = 10
        print(self._b)


obj= dervied()

