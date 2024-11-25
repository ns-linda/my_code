def over():
    s = "abcabcbb"
    maxlen = 1
    if len(s) == 0:
        return 0
    result_string=''
    for i in range(len(s)):
        substring = s[i]
        for j in range(i+1,len(s)):
            if s[i] in substring:
                substring = substring + s[j]
                # print(substring)
                maxlen = max(maxlen, len(substring))
                # print(substring, maxlen)
                if (len(substring) >= maxlen):
                    result_string = substring
            else:
                break
    return result_string, maxlen

print(over())
# # Returns the longest repeating non-overlapping
# # substring in str
# def longestRepeatedSubstring(str):
#     n = len(str)
#     dp = [[0 for x in range(n + 1)]  # Initializing dp to 0
#           for y in range(n + 1)]
#
#     ans = ""  # To store resultant substring
#     ans_len = 0  # To store length of result
#
#     # building table in bottom-up manner
#     ind = 0
#     for i in range(1, n + 1):
#         for j in range(i + 1, n + 1):
#
#             # if the characters at (i-1)th and (j-1)th
#             # position matches and codition for
#             # removing overlapping is satisfied
#             if (str[i - 1] == str[j - 1] and dp[i - 1][j - 1] < (j - i)):
#                 dp[i][j] = dp[i - 1][j - 1] + 1
#
#             # updating maximum length of the
#             # substring and updating the finishing
#             # ind of the suffix
#             if (dp[i][j] > ans_len):
#                 ans_len = dp[i][j]
#                 ind = max(i, ind)
#
#             else:
#                 dp[i][j] = 0
#
#     # If we have non-empty result, then insert
#     # all characters from first character to
#     # last character of string
#     if (ans_len > 0):
#         for i in range(ind - ans_len + 1, ind + 1):
#             ans = ans + str[i - 1]
#
#     return ans
#
#
# # Driver Code
# if __name__ == "__main__":
#     str = input("Enter the input string: ")
#     print("The longest repeating non-overlapping substring is:- ", longestRepeatedSubstring(str))
# # Sample Input 1:-
# #    Enter the input string:- opengenus
# # Sample Output 1:-
# #    The longest repeating non-overlapping substring is:- en
# # Sample Input 2:-
# #    Enter the input string:- aaaaaa
# # Sample Output 2:-
# #    The longest repeating non-overlapping substring is:- aaa
#
