l=[1,2,3,4,5,6,7,8,9,1,2]
six=[i for i, j in enumerate(l) if j==6]
nine=[k for k,l in enumerate(l) if l ==9]
print([z for z in l if z not in l[six[0]:nine[0]+1]])

remove_list=l[l.index(6):l.index(9)+1]
print([o for o in l if o not in remove_list])


def main():
    my_set = set([1, 3, 2, 4, 1, 3, 3, 0])

    # add 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 to my_set
    set2 = {10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}
    my_set = set2 | my_set

    # delete 2 and 3 from my_set
    my_set.remove(0)
    li = list(my_set)
    li.sort()

    print(li)
    return 0


if __name__ == '__main__':
    main()


def main():
    my_list = [['a', 'b'], ['cc', 'dd', ['eee', 'fff']], ['g', 'h']]

    # insert a new list [1, 2, 3] at the end of my_list
    # Your code goes here
    my_list.extend([[1, 2, 3]])
    print(my_list)

    # Delete 'eee' from the list
    # Your code goes here
    x = my_list[1][2][0]
    my_list[1][2].remove('eee')
    print(my_list)
    return 0


if __name__ == '__main__':
    main()
