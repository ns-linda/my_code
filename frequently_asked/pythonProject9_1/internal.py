#####palindrome

get_string = input("enter the string\n")
if (get_string == get_string[::-1]):
    print(get_string + " is a palindrome")
else:
    print(get_string + " is NOT a palindrome")

###prime number: 2,3,5
# n = int(input("enter the number\n"))
def find_prime(n):
    for i in range(2,n):
        if n%2 == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is  a prime number")
numbers = [1, 2, 3, 4, 5, 6, 7, 29]
for i in range(len(numbers)):
    x=find_prime(numbers[i])



