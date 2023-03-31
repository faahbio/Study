def dup(number):

    return (number * 2)


def triple(number):

    return (number * 3)


def quadup(number):

    return (number * 4)


print(dup(2))
print(triple(4))
print(quadup(6))

# --------------------------------------------------


def multiply(multiplier):

    def do_multiply(number):

        return number * multiplier

    return do_multiply


dup = multiply(2)
triple = multiply(3)
quadup = multiply(4)

print(dup(2))
print(triple(4))
print(quadup(6))
