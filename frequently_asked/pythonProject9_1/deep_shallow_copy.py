from copy import deepcopy , copy

l1=[1, 2, [3, 5], 4]
l2=l1.copy()
l2[2].append(8)
print(l1)

l3=deepcopy(l1)
l3[2].append(9)
print(l1)
print(l3)