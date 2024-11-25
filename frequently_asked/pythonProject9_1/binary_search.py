pos=-1
def binary_search(arr,n):

    mid=0
    l=0
    u=len(arr)-1
    while l <= u:
        mid = (l+u)//2
        if arr[mid] ==n:
            globals()['pos'] = mid
            return True
        else:
            if arr[mid] < n:
                l= mid+1
                print(l,"u")
            else:
                u=mid-1
                # print(u)

arr= [4,7,8,12,45,99]
if binary_search(arr,99):
    print(pos)
else:
    print("Not foud")
