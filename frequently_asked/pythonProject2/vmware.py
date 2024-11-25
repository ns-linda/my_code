S = 'i.like.this.program.very.much'
a=[]
for i in S.split("."):
    a.append(i)
b=((a[::-1]))
# print(".".join(b))
# print(".".join(S.split(".")[::-1]))
geek = ['geeksforgeeks', 'geeks', 'geek',
         'geezer']
# SI = ["the", "quick", "brown", "fox",
#      "quick"]
count = 0
# word1 = "the"
# word2 = "fox"
# SI=["geeks", "for", "geeks", "contribute",
#      "practice"]
# word1 = "geeks"
# word2 = "practice"
# for word1 in SI:
#     for
#     if i == word1:
#         count =0
#     elif i != word2:
#         count +=1
#     else:
#         pass
# print(count)
m={'a': 100, 'b': 200, 'c': 300}
g=int()
for o,p in m.items():
    g= g+p
print(g)
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
h=[]
for i in ar1:
    if i in ar2:
        h.append(i)
    elif i in ar3:
        h.append(i)
print(h)
input =['john','johnny','jackie','johnny',
            'john','jackie','jamie','jamie',
            'john','johnny','jamie','johnny',
            'john']
f={}
for g in input:
    print(g,":",input.count(g))
    f[g]=input.count(g)
print(f)
print(max(f))

Tv = {'BreakingBad':100, 'GameOfThrones':1292, 'TMKUC' : 88}
key = max(tv, key = lambda x: Tv(x))
