import re


def validate_email(email):
    reg_pattern = '[a-z0-9]+@+[a-z0-9]+.[a-z{2,3}]'
    if re.search(reg_pattern, email):
        return True
    else:
        return False

L = []
N = int(input())
for i in range(N):
    # L.append(i)
    print(validate_email(input()))
