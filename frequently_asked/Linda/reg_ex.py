str = "d 10.116.1.216 sfd 2.2.2.3 sdfsdf  192.168.0.1"

import re

print(re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',str))

string = "In 2020, the avg temperatures in bangalore were variying from 15-25.30. The humidity also increased from 50.5% to 70.24%."

listc1= re.findall('\d\+\.?\d*',string)
listc= re.findall("[0-9]+\.?[0-9]+",string)
print(listc)
print(listc1)

# Python program to validate an Ip address

# re module provides support
# for regular expressions
import re
regex = "^((25[0-5]|2[0-4][0-9]|1[1-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[1-9][0-9]|[1-9]?[0-9])"
def check(Ip):
    if (re.search(regex, Ip)):
        print("Valid Ip address")
    else:
        print("Invalid Ip address")

if __name__ == '__main__':
    Ip = "192.168.0.1"
    check(Ip)
    Ip = "110.234.52.124"
    check(Ip)
    Ip = "366.1.2.2"
    check(Ip)

# without regex
# Python program to verify IP without using RegEx

# explicit function to verify IP
def isValidIP(s):
    if s.count('.') != 3:
        return 'Invalid Ip address'
    l = s.split(".")

    for ele in l:
        if int(ele) < 0 or int(ele) > 255 or (ele[0]=='0' and len(ele)!=1):
            return 'Invalid Ip address'    
    return 'Valid Ip address'
print(isValidIP('110.234.52.124'))
