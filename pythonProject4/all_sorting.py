def bubble(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr
def selection(arr):
    for i in range(len(arr)):
        for j in range(i):
            if arr[i]<arr[j]:
                arr[i], arr[j]= arr[j], arr[i]
    return arr

def insertion(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]> key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr
def merge(arr):
    if len(arr)>1:
        r=len(arr)//2
        L=arr[:r]
        M=arr[r:]
        merge(L)
        merge(M)
        i=k=j=0
        while i < len(L) and j< len(M):
            if L[i] < M[j]:
                arr[k]=L[i]
                i=i+1
            else:
                arr[k]=M[j]
                j=j+1
            k=k+1

        while i < len(L):
                arr[k]=L[i]
                i=i+1
                k=k+1
        while j< len(M):
                arr[k]=M[j]
                j=j+1
                k=k+1
    return arr
def partition(arr, low, high):
    pivot=arr[high]
    i=low-1
    for j in range(low, high):
        if arr[j]<=pivot:
            i = i + 1
            arr[i], arr[j]=arr[j], arr[i]
    arr[i+1], arr[high]= arr[high], arr[i+1]
    return i+1
def quick_sort(arr, low, high):
    if low <=high:
        pi=partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

def binary_searc(arr, low, high, x):
    if low <high:
        mid = (low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid] > x:
            return binary_searc(arr, low, mid-1, x)
        else:
            return binary_searc(arr, mid+1, high, x)

print(bubble([3, 8, -1, 5, 9, -6, 4, 5]))
print(selection([3, 8, -1, 5, 9, -6, 4, 5]))
print(insertion([3, 8, -1, 5, 9, -6, 4, 5]))
print(merge([3, 8, -1, 5, 9, -6, 4, 5]))
arr=[3, 8, -1, 5, 9, -6, 4, 5]
quick_sort(arr, 0, len(arr)-1)
print(arr)

arr = [2, 3, 4, 10, 40]
x = 10
print(binary_searc(arr, 0, len(arr)-1, x))