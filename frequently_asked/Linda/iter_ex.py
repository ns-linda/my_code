class Arraylist:

    def __init__(self, arrayl):
        self.arrayl = arrayl

    def __iter__(self):
        self.pos =0
        return self

    def __next__(self):
        if self.pos < len(self.arrayl):
            self.pos +=1
            return self.arrayl[self.pos-1]

obj= Arraylist([1,2,3])
it=iter(obj)
print(next(it))
print(next(it))
print(next(it))
