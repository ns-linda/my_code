def sort(arr):

    # for i in range(len(arr)-1,0,-1):
    #     for j in range(i):
    #         if arr[j] > arr[j+1]:
    #             temp = arr[j]
    #             arr[j]= arr[j+1]
    #             arr[j+1]=temp
    #
    # for i in range(len(arr)):
    #     for j in range(i+1, len(arr)):
    #         if arr[i] > arr[j]:

    #             arr[j], arr[i]= arr[i], arr[j]
    # print(arr)
    # for i in range(len(arr)):
    #     for j in range(i+1):
    #         if arr[i] < arr[j]:
    #             arr[i], arr[j] = arr[j], arr[i]
    # print(arr)
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j]> arr[j+1]:
                temp= arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    print(arr)

nums=[6,2,4,3,1,1,2]
sort(nums)
print(nums)