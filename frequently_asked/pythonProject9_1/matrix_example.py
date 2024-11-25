# def find_smallest_largest(matrix):
#     small = matrix[0][0]
#     larg = matrix[0][0]
#     for i in range(row_count):
#         for j in range(col_count):
#             if small > matrix[i][j]:
#                 small =matrix[i][j]
#
#         for j in range(col_count):
#             if larg < matrix[i][j]:
#                 larg =matrix[i][j]
#     print("smallest is", small)
#     print("largest is", larg)
#
#
# if __name__ == '__main__':
#
#     row_count = int(input())
#     col_count = int(input())
#     matrix=[]
#     for i in range(row_count):
#         a=[]
#         for j in range(col_count):
#             a.append((int(input())))
#         matrix.append(a)
#     print(matrix)
#     find_smallest_largest(matrix)

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