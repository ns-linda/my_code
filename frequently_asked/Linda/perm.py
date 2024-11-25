lst =[1,2,3,4]
from itertools import permutations
print(list(permutations(lst)))

ini_str='abc'
result=[]
def perm(data,i, l):
    if i==l:
        result.append(''.join(data))
    else:
        for j in range(i,l):
            data[i], data[j] = data[j], data[i]
            perm(data, i+1, l)
            data[i], data[j] = data[j], data[i]

    return result

perm(list(ini_str),0, len(ini_str))
print(result)