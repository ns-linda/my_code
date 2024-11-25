class A(object):
    def __init__(self, a):
        self.num = a

    def mul_two(self):
        self.num *= 2


class B(A):
    def __init__(self, a):
        A.__init__(self, a)

    def mul_three(self):
        print(self.num)
        self.num *= 3


obj = B(4)
print(obj.num)

obj.mul_two()
print(obj.num)

obj.mul_three()
print(obj.num)

arr = [1, 2, 40, 3, 9, 4]
N = 3
for l in range(len(arr)):
    for j in  range(l):
        z=arr[l]+arr[j]
        # print(z, end="")
        if z==N:
            print(arr[l], arr[j])


def print_pairs(arr, N):
    # hash set
    hash_set = set()

    for i in range(0, len(arr)):
        val = N - arr[i]
        if (val in hash_set):  # check if N-x is there in set, print the pair
            print("Pairs " + str(arr[i]) + ", " + str(val))
        hash_set.add(arr[i])


# driver code
arr = [1, 2, 40, 3, 9, 4]
N = 3
print_pairs(arr, N)


def check_distinct(l):
    k=list(set(l))
    if len(k) == len(l):
        return True
    else:
        return False
print(check_distinct([2,2,5,5,7,8]))