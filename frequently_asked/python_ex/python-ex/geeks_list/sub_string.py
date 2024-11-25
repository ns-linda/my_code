test_list = ["geeks4u", "allbest", "abcdef"]
substr_list = ["s4u", "est", "al", "ge", "ek", "def", "lb"]
k = 3 

for i in test_list:
    count = 0
    for j in substr_list:
        if j in i:
            count +=1
    print(i, count)
    if count ==3:
        print(i)
