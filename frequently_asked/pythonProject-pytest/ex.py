def read_data():
    male={}
    female={}
    with open("test_file.csv", 'r') as csvfile:
        for line in csvfile:
            splitline = line.split(',')
            if splitline[2].strip() == 'Male':
                male[splitline[0]] = int(splitline[1].strip())
            elif splitline[2].strip() == 'Female':
                female[splitline[0].strip()] = int(splitline[1].strip())
        male_sorted = sorted(male.values())[0:3]
        female_sorted = sorted(female.values())[0:3]
        print(male_sorted)
        print(female_sorted)
        for i, j in male.items():
            if j in male_sorted:
                print(i,j)
        for i,j in female.items():
            if j in female_sorted:
                print(i,j)
read_data()

list = [3, 2, 5, 1, 8, 7]
rotation=3
for j in range(rotation):
    temp = list[0]
    for i in range(len(list)):
        if i+1 == len(list):
            list[i]=temp
            print(list)
            break
        list[i]=list[i+1]
        #print(list)
list1 = [3, 2, 5, 1, 8, 7]
for j in range(rotation):
    temp = list1[len(list1)-1]

    for i in range(len(list1)-1, 0, -1):

        list1[i]= list1[i-1]
    list1[0]=temp

print(list)