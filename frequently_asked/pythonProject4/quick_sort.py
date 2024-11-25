# def partition(arr,low,high):
#     pivot = arr[high]
#     i = low-1
#
#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i+1
#             (arr[i], arr[j])= arr[j], arr[i]
#     (arr[i+1], arr[high])=(arr[high], arr[i+1])
#     # print(arr)
#     return i+1
#
#
#
# def quick_sort(arr, low, high):
#     if low < high:
#
#         pi = partition(arr, low, high)
#         quick_sort(arr,low, pi-1)
#         quick_sort(arr, pi+1,high)





# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low -1
#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i=i+1
#             (arr[i], arr[j]) = (arr[j], arr[i])
#     (arr[i+1], arr[high]) = (arr[high], arr[i+1])
#
#     return i+1
#
#
# def quick_sort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         quick_sort(arr,low, pi-1)
#         quick_sort(arr, pi+1, high)


# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low-1
#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i=i+1
#             (arr[i], arr[j])= (arr[j], arr[i])
#     (arr[i+1], arr[high]) = (arr[high], arr[i+1])
#     return i+1
#
#
# def quick_sort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         quick_sort(arr, low, pi-1)
#         quick_sort(arr,pi+1, high)

def partition(data, low, high):
    pivot = data[high]
    i= low-1
    for j in range(low, high):
        if data[j] <= pivot:
            i=i+1
            (data[i], data[j])= (data[j], data[i])
    data[i+1], data[high]= data[high], data[i+1]
    return i+1

def quick_sort(data, low, high):
    if low < high:
        pi = partition(data, low, high)
        quick_sort(data, low, pi-1)
        quick_sort(data, pi+1, high)


data = [1,4,7,9,10,1,-2]
print(data)
quick_sort(data, 0, len(data)-1)
print(data)
