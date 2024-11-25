if __name__ == '__main__':
    l= []
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        # rec = str(name) + ',' + score
        l.append([name, score])
    print(l)