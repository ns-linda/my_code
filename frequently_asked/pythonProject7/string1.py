def print_full_name(first, last):
    # Write your code here
    a= "Hello " + first +" "+ last +"! You just delved into python."
    return str(a)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print(print_full_name(first_name, last_name))
