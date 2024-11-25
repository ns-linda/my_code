# s1 = "sdfsdfssfsdfsfsfsfgfgfagfdadssdfgsdgfdfsdfgfdfafsdgfsfsdfdssdf"
# s2 = "sdf"
s1="dalindadada"
s2="da"
print(s1.count(s2))
count=0
for i in range(len(s1)):
    if s1[i:i+len(s2)] == s2:
        count +=1
print(count)
