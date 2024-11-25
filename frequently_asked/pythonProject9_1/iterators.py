class ArrayList:
    def __init__(self,arr):
        self.arr = arr
    def __iter__(self):
        self.pos=0
        return self
    def __next__(self):
        if self.pos < len(self.arr):
            self.pos +=1
            return self.arr[self.pos-1]

array_obj = ArrayList([1, 2, 3])
it=(iter(array_obj))
print(it)
print(next(it))
print(next(it))
print(next(it))

lis = [1,2,3,4,5,6]
ele = iter(lis)
print(next(ele))
print(next(ele))
print(next(ele))
try:
    while True:
        print(next(ele))
except:
    pass
def tellArguments(**kwargs):
   for key, value in kwargs.items():
       print(key + ": " + value)
tellArguments(arg1 = "argument 1", arg2 = "argument 2", arg3 = "argument 3")