class Data:

    def read_data(self):
        dict_male={}
        dict_female={}
        with open ('test_file.csv') as csv_file:
            for line in csv_file:
                data = line.split(",")
                if data[2].strip() == 'Male':
                    dict_male[data[0]] = data[1]
                if data[2].strip() == 'Female':
                    dict_female[data[0]] = data[1]

        print(sorted(dict_male.values())[0:3])
        print(sorted(dict_female.values())[0:3])
        print("Young males are:", '\n')
        for i, j in dict_male.items():
            if j in sorted(dict_male.values())[0:3]:
                print(i,j)
        print("Young females are: \n")
        for i, j in dict_female.items():
            if j in sorted(dict_female.values())[0:3]:
                print(i,j)



obj = Data()
obj.read_data()

