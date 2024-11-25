def gen():
    n = 1
    print("first iter")
    yield n

    n +=1
    yield n

    n +=1
    yield n

for i in gen():
    print(i)

obj = gen()

# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Using for loop
for item in my_gen():
    print(item)

def fib(n):
    p,q = 0,1
    while p < n:
        yield p
        p,q = q, p+q
x=fib(10)
for k in x:
    print(k)


class itera():
    def __init__(self, arr):
        self.arr = arr

    def __iter__(self):
        self.pos = 0
        return self

    def __next__(self):
        if self.pos < len(self.arr):
            self.pos +=1
            return (self.arr[self.pos-1])

obj = itera([1,2,3])
it = iter(obj)
print(next(it))
print(next(it))