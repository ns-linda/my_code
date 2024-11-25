s = "geeksforgeeks"
# #Output: 3Explanation: The answer is "abc", with the length of 3.
stri={}
for i in range(len(s)):
    substring=""

    for j in range(i+1):
        if s[j] not in substring:
            substring = substring + s[j]
            stri[substring]=len(substring)
print(max(stri))
d={}
for i in range(len(s)):
    substring=""
    for j in range(i+1):
            substring = substring + s[j]
            d[substring]=len(substring)
for i in d.keys():
    if i in s and s.count(i)>1:
        print(i)
