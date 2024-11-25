import csv
with open("test_file.csv", 'r') as csvfile:
    reader=csv.reader(csvfile)
    m_age={}
    f_age={}
    for line in reader:
        if line[2].strip() == "Male":
            m_age[line[0]]=int(line[1])
        if line[2].strip() == "Female":
            f_age[line[0]]=int(line[1])
    m=sorted(m_age.values(), reverse=True)[0:3]
    f=sorted(f_age.values(), reverse=True)[0:3]
    print({i:j for i, j in m_age.items() if j in m})
    print({i: j for i, j in f_age.items() if j in f})


d1 = {'key1': 50, 'key2': 100, 'key3':200}
d2 = {'key1': 200, 'key2': 100, 'key4':300}
d3={key:d1.get(key,0)+ d2.get(key,0) for key in set(d1)| set(d2)}
print(d3)