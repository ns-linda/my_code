S = 'i.like.this.program.very.much'
print(['.'.join(S.split('.')[::-1])][::-1])
#print(i.split(".") for i in S )
test_list = ['Gfg is good for learning', 'Gfg is for geeks', 'l love G4G']
K = 'l'
for i in test_list:
    x=i.split()
    for j in x:
        if j[0] ==  K:
            print(j)

rev=[]
for i in S:
    rev.append(i)
print(''.join(rev))

for i in test_list:
    print(i)
    if i.startswith(K):
        print(i)

S = 'i.like.this.program.very.much'
print('.'.join((i[::-1]) for i in S.split(".")[::-1] ))

