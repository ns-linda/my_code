test_list1 = [[1, 3], [4, 5], [5, 6]]
test_list2 = [[7, 9], [3, 2], [3, 10]]
a=[]
print(len(test_list1))
for i in range(len(test_list1)):
        b=  test_list1[i]+ test_list2[i]
        a.append(b)
print(a)

Input = [[1, 5, 3],  ## 0,0 + 1,0 + 2,0
         [2, 7, 8],
         [4, 6, 9]]
Output = [7, 18, 20]

h = list(map(lambda x: sum(x),Input))
# g = list(sum(i[0][i]) for i in range(len(Input)))
print(h)
print(Input)
nw=[]
for i in range(len(Input)): ## 0,1,2
    # print(Input[i])
    sum = 0
    for j in range(0, len(Input[i])): ##0,1,2
        # print(Input[j][i])
        sum =sum + Input[j][i]
        print(sum)
    nw.append(sum)
print(nw)

