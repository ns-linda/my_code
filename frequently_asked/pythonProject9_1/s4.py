def find(s):
    maxl = 1
    substring =''
    d={}
    for i in range(len(s)):
        substring = s[i]
        for j in range(i+1,len(s)):
            if s[j] not in substring:
                substring =substring + s[j]
                maxl = max(maxl,len(substring))
                if maxl == len(substring):
                    d[substring]=maxl
            else:
                break
    return d,maxl



# r=find('GEEKSFORGEEKS')
# print(r)
# for i, j in r[0].items():
#     if j == r[1]:
#         print(i,j)

def find_common(s):
    substring =''
    maxl=1
    d={}
    for i in range(len(s)):
        substring = s[i]
        for j in range(i+1,len(s)):
            # if substring  in s[j]:
                substring = substring + s[j]
                print(substring)
                if s.count(substring) > 1:
                    maxl = max(maxl, len(substring))
                    if maxl == len(substring):
                        d[substring]=maxl
    return d

print(find_common('banana'))

