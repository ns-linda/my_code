n_d ={}
name=['linda',"wijai", "kristy"]
l=[20,21,4]
m=[0,1,2]
n=[9,8,7]
for item in range(len(name)):
    n_d[name[item]]={}
    # n_d[name[item]]=name[item]
    n_d[name[item]]['inet']= l[item]
    n_d[name[item]]['broadcast']=m[item]
    n_d[name[item]]['ethernet']=n[item]
print(n_d)



