def find_non_repeat(my_array):
    nr={}
    for i in my_array:
        if i in nr:
            nr[i]+=1
        else:
            nr[i]=1
    print(nr)

my_array = "aabbccdef"
find_non_repeat(my_array)

def find_length(s):
    substring =''
    maxl= 1
    nr={}
    for i in range(len(s)):
        substring = s[i]
        for j in range(i+1):
            if s[j] not in substring:
                substring = substring + s[j]
                # print(substring)
                nr[substring]=len(substring)
    z=max(nr.values())
    for i, j in nr.items():
        if j == z:
            print(i,j)


(find_length("geeksforgeeks"))

s = "geeksforgeeks"
##longest repeating but not overlaping
substring=''
count=0
for i in range(len(s)):
    substring = substring + s[i]
    if substring in s and s.count(substring) >1:
        print(substring)
