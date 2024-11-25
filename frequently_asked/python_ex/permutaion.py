def perm(s):
    if len(s) == 0:
        return []
    elif len(s) == 1:
        return [s]
    else:
        result=[]
        for i in range(len(s)):
            c = s[i]
            rem = s[:i] + s[i+1:]
            for p in perm(rem):
                result.append(c+p)
                print
    return (result)


s='abc'
per=perm(s)
for p in per:
    print(''.join(p))