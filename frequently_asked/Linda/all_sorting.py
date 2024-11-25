##bubble sort
def sorting(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[i] < arr[j]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    print(arr)

def bubble(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]> arr[j+1]:
                temp = arr[j]
                arr[j]= arr[j+1]
                arr[j+1]=temp
    print(arr)

arr= [6,2,4,3,1,1,2]
bubble(arr)

##selectionsort
def selection(arr):
    for i in range(len(arr)):
        for j in range(i+1):
            if arr[i] < arr[j]:
                arr[i], arr[j]= arr[j], arr[i]
    print(arr)
arr= [6,2,4,3,1,1,2]
selection(arr)

##insertion_sort:
def insertion(list):
    for i in range(1,len(list)):
        key = list[i]
        j=i-1
        while j>=0 and key < list[j]:
            list[j+1]=list[j]
            j=j-1
            list[j+1]=key
    print(list)

list = [3, 8, -1, 5, 9, -6, 4, 5]
insertion(list)

##merge_sort
def mergeSort(alist):
    print(alist)
    if len(alist)>1:
        mid= len(alist)//2
        lefthalf=alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        while i< len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print(alist)

##QUICKsort
def parition(arr,low, high):
     pivot=arr[high]
     i=low-1
     for j in range(low, high):
         if arr[j] < pivot:
             i=i+1
             (arr[i], arr[j])= (arr[j], arr[i])
     (arr[i+1], arr[high])= (arr[high], arr[i+1])
     return i+1

def quick_sort(arr, low, high):
    if low < high:
        pi = parition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1,high)

arr= [3,4,5,-1,8,10]
quick_sort(arr, 0, len(arr)-1)
print(arr)

##binary search: it has to be sorted
def binary(arr, low, high, x):
    # if low <=high:
    if high >=low:
        mid = (low+high)//2
        if arr[mid] ==x:
            return mid
        elif arr[mid] > x:
            return binary(arr, low, mid-1, x)
        else:
            return binary(arr, mid+1, high, x)
    # else:
    #     return -1

arr= [ 2,10, 3, 4, 1, 40 ]
print(binary(arr, 0, len(arr)-1, 10))


