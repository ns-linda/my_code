# s=[0, -1, 2, -3, 1]
# num=0
# for i in range(len(s)):
#     for j in range(i+1, len(s)):
#         for z in range(j+1, len(s)):
#              f=  s[i]+ s[j] + s[z]
#              if f==0:
#                 print(s[i], s[j], s[z])
#
# dict = ["pintu", "geeksfor", "geeksgeeks", "forgeek"]
# str = "geeksforgeeks"
# substring =''
# maxl=1
# k={}
#
# for item in dict:
#     substring = ''
#     for i in str:
#         if i in item:
#             substring = substring + i
#             if substring == item:
#                 print(substring, len(substring))
#                 maxl = max(maxl, len(substring))
#                 if maxl == len(substring):
#                     k[substring]=maxl
#
#         else:
#             continue
#             # k.pop(i)
# print(k)

def find(s):
    substring =''
    maxl = 1
    for i in range(len(s)):
        substring = ''
        for j in range(i+1,len(s)):
                substring = s[i] + s[j:]
                maxl = max(maxl, len(substring))
    print(maxl)

find('aabbcc')

def longest_substring(s):
    maxl = 1
    longest_substring = {}
    for i in range(len(s)):
        substring =s[i]
        for j in range(i+1, len(s)):
            if s[j] not in substring:
                substring += s[j]
                # print(substring)
                maxl = max(maxl, len(substring))
                longest_substring[substring] = maxl
    return maxl, longest_substring

print(longest_substring('aabbcc'))

