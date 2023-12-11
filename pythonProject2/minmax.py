import os


# def findminmax(arr):
#     l=[]
#     for num in arr:
#         sumi = sum(arr)-num
#         l.append(sumi)
#     print(l)
#     print(min(l)+ " "+ max(l))
#     print(max(l))
#
#
#
# findminmax([1,2,3,4,5])

def lonelyinteger(a):
    # Write your code here
    c = []
    for i in a:
        print(i)
        print(a)
        if i not in c:
            c.append(i)
        else:
            c.remove(i)
    print(c)
    return c


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'junk.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)
    for i in result:
        result = i
        print(result)
        fptr.write(str(result) + '\n')

    fptr.close()