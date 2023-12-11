Input= ['cat', 'dog', 'cat', 'god']
temp = [''.join(sorted(i)) for i in Input]
print(temp)
new_l = {}


for i in set(temp):
    ind = [j for j, x in enumerate(temp) if x == i]
    #print(ind)
    tempout = []
    for k in ind:
        #print(k)
        tempout.append(Input[k])
print(tempout)

def check(s1,s2):
    if sorted(s1) == sorted(s2):
        print("yes")

s1 ="listen"
s2 ="silent"
check(s1, s2)




