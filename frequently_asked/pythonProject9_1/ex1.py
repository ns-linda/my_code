def find_sum(l1):
    a=0
    for item in l1:
        # print(item)
        if isinstance(item, list):
            b = find_sum(item)
            if isinstance(b, list):
                c = find_sum(b)
                a = a + c

            else:
                a = a + b
        else:
            a = a+ item
    return a

l1= [[4,5],[7,8,[20]],100]
print(find_sum(l1))

a=[1,2,3]
step, size = 2, 4


def summing(l1):
    a=0
    for item in l1:
        if isinstance(item, list):
            a += summing(item)
        else:
            a = a+item
    return a
l1= [[4,5],[7,8,[20]],100]
print(summing(l1))

