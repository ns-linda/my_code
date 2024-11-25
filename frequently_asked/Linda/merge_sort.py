# def merge_sort(arr):
#     if len(arr)>1:
#
#         r=len(arr)//2
#         L=arr[:r]
#         M=arr[r:]
#
#         merge_sort(L)
#         merge_sort(M)
#
#         i=k=j=0
#
#         while i<len(L) and j<len(M):
#             if L[i] < M[j]:
#                 arr[k] = L[i]
#                 i=i+1
#             else:
#                 arr[k] = M[j]
#                 j=j+1
#             k=k+1
#
#         while i < len(L):
#             arr[k] = L[i]
#             i = i + 1
#             k=k+1
#
#         while j < len(M):
#             arr[k] = M[j]
#             j = j + 1
#             k = k + 1
#
#
# def printlist(arr):
#     for i in range(len(arr)):
#         print(arr[i], end=",")

# def merge_sort(arr):
#     if len(arr) >1:
#         r=len(arr)//2
#         L=arr[:r]
#         M=arr[r:]
#
#         merge_sort(L)
#         merge_sort(M)
#         i=j=k=0
#         while i < len(L) and j < len(M):
#             if L[i] < M[j]:
#                 arr[k]=L[i]
#                 i=i+1
#             else:
#                 arr[k]=M[j]
#                 arr[k]=M[j]
#                 j=j+1
#             k=k+1
#
#         if i < len(L):
#             arr[k] = L[i]
#             i = i + 1
#             k=k+1
#
#         if j <len(M):
#             arr[k] = M[j]
#             j=j+1
#             k=k+1
def merge_sort(arr):
    if len(arr)>1:
        r=len(arr)//2
        L=arr[:r]
        M=arr[r:]

        merge_sort(L)
        merge_sort(M)
        i=j=k=0
        while i <len(L) and j < (len(M)):
            if L[i] < M[j]:
                arr[k]=L[i]
                i=i+1
            else:
                arr[k]=M[j]
                j=j+1
            k=k+1
        if i<len(L):
            arr[k] = L[i]
            i = i + 1
            k=k+1

        if j<len(M):
            arr[k]=M[j]
            j=j+1
            k=k+1

def printlist(arr):
    for i in range(len(arr)):
        print(arr[i], end=", ")





arr = [6, 5, 12, 10, 9, 1]
merge_sort(arr)
printlist(arr)








