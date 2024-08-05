weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
print([[str(i), weekdays.count(i)] for i in weekdays ])

a = [1, 2, 3]
print(a[-2:])

subjects = ['Python', 'Interview', 'Questions']
for i, subject in enumerate(subjects):
    print(i, subject)

a='ping'
for i in a:
    print(i, a.index(i))


a='linda'
b=''
for i in a:
    b = i+b
print(b)

#print table for 7
# for i in range(1,11):
#     print("7*" + str(i) + "=" + str(i*7))
# multiply = list(map(lambda x: x*7, i in range(1,11) ))
# print(multiply)

def check_prime(n):
    for i in range(2,n):
        if n <1:
            print(n, "is a prime")
        if n%i == 0:
            print(n, "is not a prime")
            break
    else:
        print(n, "is a prime")

n=[1,2,3,4,5,6,7,8,9,10,11]
for j in n:
    check_prime(j)

d='Hello'
g='How are you'
for i in d:
    if i in g:
        print(i)
print([i for i in d if i in g])