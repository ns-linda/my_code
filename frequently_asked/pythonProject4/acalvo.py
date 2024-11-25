import csv
import pandas
# with open("1.csv", 'a', newline='') as csvfile:
#     writer=csv.writer(csvfile)
#     a=[("Femil","40","Female")]
#     writer.writerows(a)

with open("1.csv","r") as csvf:
    reader=csv.reader(csvf)
    male_age=[]
    female_age=[]
    for line in reader:
        if line[2]=="Male":
            male_age.append(line[1])
        if line[2] == "Female":
            female_age.append(line[1])
    max_male_age = sorted(male_age, reverse=True)[0:3]
    print(max_male_age)
    max_female_age=sorted(female_age, reverse=True)[0:3]
    with open("1.csv", "r") as csvf:
        reader = csv.reader(csvf)
        print({line[0]: line[1] for line in reader if line[2]=="Male" and line[1] in max_male_age} )
    with open("1.csv", "r") as csvf:
        reader = csv.reader(csvf)
        print({line[0]: line[1] for line in reader if line[2]=="Female" and line[1] in max_female_age})
import json
with open("1.csv", "r") as csvf:
    reader = csv.DictReader(csvf)
    d={}
    i=0
    for line in reader:
        mykey = i
        d[mykey]=line
        i+=1
    print(d)
    with open("data.json", "w") as dictfile:
        # json.dump(d,dictfile, indent=4)
        dictfile.write(json.dumps(d))

