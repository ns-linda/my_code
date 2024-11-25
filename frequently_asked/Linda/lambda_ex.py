from functools import reduce


def main():
    # Use map to print the square of each numbers
    my_ints = [4, 6, 3, 9, 2, 8, 12]
    square = list(map(lambda x:x*x, my_ints))
    # Use filter to print only the names that are less than or equal to seven letters
    my_names = ["scaler", "interviewbit", "rishabh", "student", "course"]
    filtern= list(filter(lambda name : len(name)<=7, my_names))
    # Use reduce to print the product of these numbers
    my_numbers = [4, 6, 9, 23, 5]
    reduce_n = reduce(lambda x,y: x*y, my_numbers, 1)
    # Fix all three respectively.
    map_result = list(map(lambda x: x * x, my_ints))
    filter_result = list(filter(lambda name: len(name) <=7,  my_names))
    reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers, 1)
    print(square)
    print(filtern)
    print(reduce_n)
    print(map_result)
    print(filter_result)
    print(reduce_result)
    return 0


if __name__ == '__main__':
    main()