def shout(text):
    return text.upper()


def whispher(text):
    return text.lower()


def greet(func):
    greeting = func("Hi, welcome to python")
    print(greeting)
    # return func

greet(shout)
greet(whispher)

def shout(func):
    def inner(text):
        return func(text).split()
    return inner

def whispher(func):
    def inner(text):
        return func(text).lower()
    return inner

@shout
@whispher
def main(text):
    return text

print(main("hii"))


def shout(func):
    def inner():
        return func().split()
    return inner

def whispher(func):
    def inner():
        return func().lower()
    return inner

@shout
@whispher
def main():
    return "hi"

print(main())

