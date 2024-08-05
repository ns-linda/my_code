#Input : [4, 5, 5, 5, 3, 8]

def check(l1):
    for i in l1:
        for j in range(0,2):
            print(i,j)
            if l1[j] ==l1[j+1]:
                print(i)




if __name__ == "__main__":
    l1 = [4, 5, 5, 3, 3, 3]
    #check(l1)
    for i in range(len(l1)-2):
        print(i)
        if l1[i] == l1[i+1] and l1[i+1] == l1[i+2]:
            print (l1[i])