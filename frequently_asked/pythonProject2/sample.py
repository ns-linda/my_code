def check(s1,s2):
    first = sorted(s1)
    secnd = sorted(s2)
    if first == secnd:
        print("yes")
    else:
        print("No")


if __name__ == "__main__":
    s1 = 'belowin'
    s2 = 'elbow'
    check(s1,s2)
    str = "geeks quiz practice code"

    print(" ".join([i for i in str.split(" ") if i !=0 or i !=-1][::-1]))
    print(" ".join([i[::-1] for i in str.split(" ") ]))

