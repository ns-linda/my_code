def find_smalles(matrix):
    smallest=[]
    for i in range(rowcount):
        small= matrix[0][0]
        for j in range(colcount):
            if small < matrix[i][j]:
                small=matrix[i][j]
                smallest.append(small)
    return smallest
rowcount=int(input())
colcount=int(input())
matrix=[]
for i in range(rowcount):
    a=[]
    for j in range(colcount):
        a.append(int(input()))
    matrix.append(a)
print(matrix)
len(matrix)
print(find_smalles(matrix))


