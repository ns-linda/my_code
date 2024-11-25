from collections import Counter

def find_prime(i):
    for num in range(2,i): # range after 2 till the number, prove divisible by 2
        if i%num == 0:
            print(i, num)
            print(i,"its not a prime number")
            break
    else:
            print(i,"its a prime number")

numbers = [1,2,3,4,5,6,7,29]
for i in range(len(numbers)):
    x=find_prime(numbers[i])


def print_pairs(arr, N):
    # hash set
    # hash_set = set()
    #
    # for i in range(0, len(arr)):
    #     val = N - arr[i]
    #     if (val in hash_set):  # check if N-x is there in set, print the pair
    #         print("Pairs " + str(arr[i]) + ", " + str(val))
    #     hash_set.add(arr[i])
    for i in range(len(arr)-1):
        if arr[i]+arr[i+1] == N:
            print(arr[i], arr[i+1])



# driver code
arr = [1, 2, 40, 3, 9, 4,2,3]
N = 5
# print_pairs(arr, N)
# from collections import counter
d1 = {'key1': 50, 'key2': 100, 'key3':200}
d2 = {'key1': 200, 'key2': 100, 'key4':300}

new_dict = Counter(d1) + Counter(d2)
print(new_dict)
# Python code to merge dict using update() method
def Merge(dict1, dict2):
    return (dict2.update(dict1))
result={}
for key in set(d1) | set(d2):
    result[key] = d1.get(key,0) + d2.get(key,0)
print(result)

# Driver code
dict1 = {'key1': 50, 'key2': 100, 'key3':200}
dict2 = {'key1': 200, 'key2': 100, 'key4':300}

# This return None
print(Merge(dict1, dict2))

# changes made in dict2
print(dict1)



