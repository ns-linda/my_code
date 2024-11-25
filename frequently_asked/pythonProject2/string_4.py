n_l=['Gfg', 'is', 'best', 'for', 'Geeks']
res = ", ".join(n_l)
out = res.replace("G", "_").replace("e", "G").replace("_", "e")
print(out.split(","))

nw=[]
for i in n_l:
    if 'G' in i or 'e' in i:
        str = i.replace('G', 'e').replace('e', 'G')
        nw.append(str)
    else:
        nw.append(i)
print(nw)

