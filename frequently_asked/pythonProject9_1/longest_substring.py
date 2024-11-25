def find(s):
    maxl = 1
    substring =''
    d={}
    for i in range(len(s)):
        if len(s)==0:
            return False
        substring = s[i]
        for j in range(i+1,len(s)):
            if s[j] not in substring:
                substring = substring+s[j]
                # print(substring, len(substring))
                maxl = min(maxl,len(substring))
                if maxl == len(substring):
                    d[substring] = maxl
            else:
                break
    return d, maxlq


s=find('aabcbcdbca')
print(s)
for i, j in s[0].items():
    # print(s[1])
    if j == s[1]:
        print(i,j)

# m=100
# def posi(m):
#     if m >0:
#         posi(m-1)
#         print(m, end=" ")

# posi(100)


