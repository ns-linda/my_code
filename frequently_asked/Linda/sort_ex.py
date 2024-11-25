def bubble(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    print(arr)
bubble([3,2,5,7,1])

def selection(arr):
    for i in range(len(arr)):
        for j in range(i+1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    print(arr)
selection([4,3,7,8,1,0])

def insertion(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j] > key:
            arr[j+1]=arr[j]
            j=j-1
            arr[j+1]=key
    print(arr)
insertion([2,6,7,8,9,1,0])

def merge_sort(arr):
    if (len(arr))>1:
        r=len(arr)//2
        L=arr[:r]
        M=arr[r:]
        merge_sort(L)
        merge_sort(M)
        i=j=k=0
        while i< len(L) and j < len(M):
            if L[i]< M[j]:
                arr[k]=L[i]
                i=i+1
            else:
                arr[k] = M[j]
                j = j + 1
            k = k + 1
        while i<len(L):
            arr[k]=L[i]
            i=i+1
            k=k+1

        while j < len(M):
            j = j + 1
            k = k + 1
    print(arr)
merge_sort([5,3,4,2,1,0])

def partition(arr, low, high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j] < pivot:
            i=i+1
            (arr[i], arr[j])=(arr[j], arr[i])
    (arr[i+1], arr[high])= (arr[high], arr[i+1])
    return i+1

def quick_sort(arr, low, high):
    if low < high:
        pi=partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

arr=[5,4,3,6,1,0]
quick_sort(arr, 0, len(arr)-1)
print(arr)