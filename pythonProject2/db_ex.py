#import MySQLdb
# import sys
# localhost=\
# username=\
# password=\
# dbname =\
#
# def conn():
#     try:
#         db=[]
#         # db=MySQLdb.connect(localhost, username, password, dbname)
#     except:
#         sys.exit()
#
#     cursor = db.cursor()
#     query = "select application_name from application"
#     cursor.execute(query)
#     app_name = cursor.fetchall()
#     ### for insert, alter
#     db.commit()
#     db.close()

import os
def isPangram(pangram):
    # Write your code here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # for char in alphabet:
    for i in pangram:
        for char in alphabet:
            print(i)
            if char not in i.lower():
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
    print(pangram_item)
    if (isPangram(pangram) == True):
            print("1")
    else:
            print("0")



        # fptr.write(result + '\n')

    fptr.close()

