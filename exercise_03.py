first_number = input('Digite um valor: ')
second_number = input('Digite outro valor: ')

if first_number > second_number:
    print(
        f'The first number: {first_number}, is bigger than the second number: {second_number}')

elif second_number > first_number:
    print(
        f'The second number: {second_number}, is bigger than the first number: {first_number}')

else:
    print(f'The numbers are the same, {first_number} and {second_number}')
