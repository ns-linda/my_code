a=[15, -2, 2, -8, 1, 7, 10, 23]
maxl = 0

for i in range(len(a)):
    current_sum = 0
    for j in range(i, len(a)):
        print(a[j], end=", ")
        current_sum +=a[j]
        # print(current_sum, end =", ")
        if current_sum ==0:
            print(a[j])



