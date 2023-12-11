my_dict = {1 : 1, -3 : 9, 2 : 4, -5 : 25, 4 : 16}
print(min(my_dict, key = lambda x: my_dict[x]))

class Solution:
    def twoSum(self, nums, target):
        # declaring a dictionary to keep track of all the values
        visited_numbers = dict()

        # iterating over the entire array
        for index, num in enumerate(nums):

            # subtracting the num from the target to search for its pair
            number_to_be_search = target - num

            # if the pair is found, return the index of the both numbers
            if number_to_be_search in visited_numbers:
                print(num, number_to_be_search)
                # return [index, visited_numbers[number_to_be_search]]

                # otherwise we simply add it to out dictionary for future lookup
            else:
                visited_numbers[num] = index
        # print(visited_numbers)

list1 = [2, 7, 11, 15,18,0]
target = 18
obj = Solution()
obj.twoSum(list1, target)



