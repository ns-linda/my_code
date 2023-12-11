# def RotateSentence(sentence, n):
#     words = sentence.split()
#     lengths = [len(w) for w in words]
#     print(lengths)
#     s = ''.join(words)
#     s = s[-n:] + s[:-n]
#     res = ''
#     i = 0
#     for l in lengths:
#         if res:
#             res += ' '
#         res += s[i:i+l]
#         i += l
#         print(i)
#     return res
#
# def _main():
#     s = input()
#     n = int(input())
#     s = RotateSentence(s, n)
#     print(s)
#
# if __name__ == '__main__':
#     _main()

def rotate(s,n):
    words = s.split()
    length= [len(i) for i in words]
    s="".join(words)
    s= s[-n:]+ s[:-n]
    i=0
    res=''
    for l in length:
        if res:
            res +=' '
        res += s[i:i+l]
        i +=l
    return res

print(rotate("am linda", 1))

l=[2,4,5,6,7,8]
for i in range(2):
    temp=l[0]
    for j in range(len(l)):
        if j+1== len(l):
            # l[j]=l[j+1]
            l[j]=temp
            break

        l[j]=l[j+1]
print(l)
l=[2,4,5,6,7,8]
for i in range(2):
    temp=l[len(l)-1]
    for j in range(len(l)-1,0,-1):
        l[j]=l[j-1]
    l[0]=temp
print(l)
#
# def pprint(**kwargs):
#     for i,j in kwargs.items():
#         print(i)
# items= (int(input()))
# l={}
# for i in range(items):
#     l["key"+str(i)]=input()
# print(l)
# pprint(key1="hi", key2="hello")

arr = [1, 2, 40, 3, 9, 4,0]
N = 3
n={}
for i in range(len(arr)):
    val= N-arr[i]
    if val in n.values():
        print(val, arr[i])
    else:
        n[i]=arr[i]

def add(num1, num2):
    while num2 !=0:
        data = num1 & num2
        num1 = num1 ^num2
        num2 = data << 1
    return num1
print(add(2,3))