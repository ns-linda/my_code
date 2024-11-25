import multiprocessing

def cube(num):
    print("cube is {}".format(num*num *num))

def square(num):
    print("square is {}".format(num * num))


if __name__ ==  '__main__':
    t1 = multiprocessing.Process(target=cube, args=(10,))
    t2 = multiprocessing.Process(target=square, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

