import os
def isPangram(pangram):
    # Write your code here
    # print(pangram)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char not in pangram.lower():
                return False
    return True

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'junk.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pangram_count = int(input().strip())

    pangram = []

    for _ in range(pangram_count):
        pangram_item = input()
        pangram.append(pangram_item)
    for i in range(len(pangram)):
        result = isPangram(pangram[i])
        print(result)
        if result == False:
            result = "0"
        else:
            result ="1"
        fptr.write(result + '\n')

    fptr.close()
