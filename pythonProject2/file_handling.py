with open ("sample.txt", 'w') as file:
    file.write("1,2,3\n4,5,6")

f = open("sample.txt", "r")
print(f.read())
for line in f:
    print(line)
