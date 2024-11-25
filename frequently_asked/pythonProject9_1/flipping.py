import os
def flippingMatrix(matrix):
    # Write your code here
    length = len(matrix)
    n = int(length/2)
    sum = 0
    for r in range(n):
        for c in range(n):
            sum += max([matrix[r][c], matrix[r][length-1-c], matrix[length-1-r][c], matrix[length-1-r][length-1-c],])
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()