#
# def find_largest(matrix):
#     largest = []
#     for i in range(row_count):
#         larg = matrix[0][0]
#         for j in range(col_cout):
#             if larg < matrix[i][j]:
#                 larg =matrix[i][j]
#                 largest.append(larg)
#     return largest
#
# def smallest(matrix):
#     smallest = []
#     for i in range(row_count):
#         small = matrix[0][0]
#         for j in range(col_cout):
#             if small > matrix[i][j]:
#                 small = matrix[i][j]
#                 smallest.append(small)
#     return smallest
#
# row_count= int(input())
# col_cout = int(input())
# matrix=[]
# for i in range(row_count):
#     a=[]
#     for j in range(col_cout):
#         a.append(int(input()))
#     matrix.append(a)
# print(matrix)
# print(find_largest(matrix))
# print(smallest(matrix))

def find_largest_in_row_smallest_in_column_in_matrix(matrix):
    largest_list=[]
    smallest_list=[]
    row_count=len(matrix)
    col_count=len(matrix[0])

    for i in range(row_count):
        largest=matrix[0][0]
        for j in range(col_count):
            if largest<matrix[i][j]:
                largest=matrix[i][j]
        largest_list.append(largest)
    smallest = matrix[0][0]
    for i in range(col_count):

        for j in range(row_count):
            a=matrix[j][i]
            if smallest>matrix[j][i]:
                smallest=matrix[j][i]
        smallest_list.append(smallest)
    print(smallest_list)
    print(largest_list)
    for i in smallest_list:
        if i in largest_list:
            return i
    return -1

if __name__ =="__main__":
    row_count= int(input())
    col_count= int(input())
    matrix=[]
    for i in range(row_count):
        a = []
        for j in range(col_count):
            a.append(int(input()))
        matrix.append(a)

    # for i in range(row_count):
    #     iterator = list(map(int, input().rstrip().split()))
    #     matrix.append(iterator)
    result=find_largest_in_row_smallest_in_column_in_matrix(matrix)
    print(result)
