def split_and_join(line):
    # write your code here
    covert_to_list = line.split(" ")
    a = "-".join(covert_to_list)
    return a


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)