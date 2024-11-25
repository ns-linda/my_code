#bubble
def bubble(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    print(arr)


arr=[9,8,4,6,3,2,1]
bubble(arr)

#insertion
def insertion(arr):
    for i in range(len(arr)):
        key = arr[i]
        j=i-1
        while j >=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    print(arr)
insertion([9,8,4,6,3,2,1])

alist=['cat' ,'cat', 'dog' ,'cat', 'hen', 'hen']
d={}
for i in alist:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)

def selection(arr):
    for i in range(len(arr)):
        for j in range(i+1):
            if arr[i]<arr[j]:
                arr[i], arr[j]= arr[j],arr[i]
    print(arr)
selection([9,8,4,6,3,2,1])

def partition(arr, low, high):
    pivot=arr[high]
    i=low-1
    for j in range(low, high):
        if arr[j]< pivot:
            i=i+1
            arr[i], arr[j]=arr[j], arr[i]
    arr[i+1], arr[high]=arr[high], arr[i+1]
    return i+1

def quicksort(arr, low, high):
    if low < high:
        pi=partition(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)

arr=[9,8,4,6,3,2,1]
quicksort(arr, 0, len(arr)-1)
print(arr)

#merge
def merge(arr):
    if len(arr) > 1:
        r=len(arr)//2
        L=arr[:r]
        M=arr[r:]
        merge(L)
        merge(M)
        i=j=k=0
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                arr[k]=L[i]
                i=i+1
            else:
                arr[k] = M[j]
                j = j + 1
            k=k+1

        while i < len(L):
                arr[k]=L[i]
                i=i+1
                k=k+1
        while j < len(M):
            arr[k] = M[j]
            j = j + 1
            k = k + 1
arr=[9,8,4,6,3,2,1]
merge(arr)
print(arr)

#binary search
def binary(arr, low, high, x):
    if low <=high:
        mid = (low+high)//2
        if x== arr[mid]:
            return mid
        else:
            if x< arr[mid]:
                return binary(arr, low, mid-1, x)
            else:
                return binary(arr, mid + 1,high, x)
    else:
        return -1


arr = [ 2, 3, 4, 10, 40 ]
x = 40
print(binary(arr, 0, len(arr)-1, x))

