def test_substring(s1, s2):
    l=len(s2)
    count=0
    for i in range(len(s1)):
        print(s1[i:i+l], end=",")
        if s1[i:i+l] == s2:
            count +=1
    print(count)
s1 = "sdfsdfssfsdfsfsfsfgfgfagfdadssdfgsdgfdfsdfgfdfafsdgfsfsdfdssdf"
s2 = "sdf"
print(s1.count(s2))
test_substring(s1, s2)

s='aaabcffgh'
print("".join([i for i in s if s.count(i)==1]))
n=""
for i in s:
    if i not in n:
        n+=i
print(n)