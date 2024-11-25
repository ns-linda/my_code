# def partition(arr, low, high):
#     pivot = arr[high]
#     i= low-1
#
#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i=i+1
#             (arr[i], arr[j])=(arr[j], arr[i])
#
#     (arr[i+1], arr[high]) = (arr[high], arr[i+1])
#     return i+1
#
# def quick_sort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         quick_sort(arr, low, pi-1)
#         quick_sort(arr, pi+1, high)

def parition(arr, low, high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i=i+1
            (arr[i], arr[j])=(arr[j], arr[i])
    (arr[i+1], arr[high])=(arr[high], arr[i+1])
    return i+1

def quick_sort(arr, low, high):
    if low <high:
        pi= parition(arr,low,high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

arr=[1,4,5,2,3]
quick_sort(arr,0, len(arr)-1)
print(arr)

# def binary_search(arr, low, high, x):
#     if high >=low:
#         mid = high +low //2
#
#         if arr[mid]==x:
#             return mid
#         elif arr[mid] > x:
#             return binary_search(arr, low, mid-1,x)
#         else:
#             return binary_search(arr, mid+1,high, x)
#     else:
#         return -1
def binary_search(arr, low, high, x):
    if low <=high:
        mid=high+low//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr, low, mid-1,x)
        else:
            return binary_search(arr, mid+1, high,x)
    else:
        return-1
data=[ 2, 3, 4, 10, 40]
res=binary_search(data, 0, len(data)-1, int(10))
print(res)