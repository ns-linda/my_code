test_list = [6,3,5,3]
l=[]
for i in test_list:
    if i in l:
        l.remove(i)
    else:
        l.append(i)
print(l)

test_dict = {1: ['gfg', 'CS', 'cool'], 2: ['gfg', 'CS']}
freq = {}
for i in test_dict.values():
    for j in i:
        if j in freq:
            freq[j] +=1
        else:
            freq[j]=1
print(freq)

L= [1,2,[3,5],3,1]


mydict={'e':5,'b':12,'a':1,'c':3}
n={}
sorted_val = sorted(mydict.values())
for i in sorted_val:
    for k in mydict.keys():
       if mydict[k] == i:
        n[k]=i

print(n)


def find_sum(L):
    a=0
    for item in L:
        if isinstance(item, list):
            print(item)
            b = find_sum(item)
            print(b)
            a= a+b
        else:
            a = item + a
    return a

L= [1,2,[3,5],3,1]
print(find_sum(L))
