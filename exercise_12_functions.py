# --------------------------------------------------
# There are two different codes here
# Comment the code you don't want to use
# --------------------------------------------------

def even_odd(number):

    if (number % 2) == 0:

        return "Even"

    return "Odd"


number = input('Type a number: ')

try:

    number = int(number)
    print(f'The number {number} is', even_odd(number))

except:

    print("You didn't type an integer number")

# --------------------------------------------------


def multiply(*args):

    total = 1

    for arg in args:

        total *= arg

    return total


print(multiply(1, 2, 3, 4, 5))
