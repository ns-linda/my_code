def b(arr):
    # for i in range(len(arr)-1,0,-1):
    #     for j in range(i):
    #         if arr[j] > arr[j+1]:
    #             temp = arr[j]
    #             arr[j]= arr[j+1]
    #             arr[j+1]=temp
    # print(arr)
    for i in range(len(arr)):
        for j in range(i+1):
            if arr[i]<arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    print(arr)

arr= [6,2,4,3,1,1,2]
b(arr)