
def is_valid(ip):

    # Splitting by "."
    ip = ip.split(".")

    # Checking for the corner cases
    for i in ip:
        if len(i) > 3 or int(i) < 0 or int(i) > 255:
            return False
        if len(i) > 1 and int(i) == 0:
            return False
        if len(i) > 1 and int(i) != 0 and i[0] == '0':
            return False
    return True

if __name__ == '__main__':
    get_ip = input("enter the ip")
    if is_valid(get_ip):
        print("valid")
    else:
        print("Invalid")