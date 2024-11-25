sentence = 'Jim quickly realized that the beautiful Gowns are expensive'
count_letters = {}
cnt_lowercase = 0
cnt_uppercase = 0
for i in sentence:
    if i.isupper():
        cnt_uppercase +=1
    if i.islower():
        cnt_lowercase +=1
count_letters['upper']= cnt_uppercase
count_letters['lower']= cnt_lowercase
print(count_letters)


sentence = 'Jim quickly realized that the beautiful Gowns are expensive'
count_upper = 0
count_lower =0
dict_1 = {}

def isPangram(pangram):
    # Write your code here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        for i in pangram:
            if char not in i.lower():
                return "0"
            else:
                return "1"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pangram_count = int(input().strip())

    pangram = []

    for _ in range(pangram_count):
        pangram_item = input()
        pangram.append(pangram_item)

    result = isPangram(pangram)

    fptr.write(result + '\n')

    fptr.close()

for i in sentence.split(" "):
    if i.isupper():
        count_upper += 1
    elif i.islower():
        count_lower +=1
    dict_1["upper"] =  count_upper
    dict_1["lower"] = count_lower
print(dict_1)







