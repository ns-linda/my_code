#do iteration only what is required

def topten():
    n = 1
    while n <=10:
        sq = n*n
        yield sq #unlike return yield will not terminate the function
        n=n+1

val = topten()
for i in val:
    print(i)