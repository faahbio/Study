"""
First you need to ask the user for an int number, than you should tell if the number is ever or odd.
If the number is not an int, tell the user that.
"""

number = input('Tell me a integer number: ')

if number.isdigit:

    if (int(number) % 2) is 0:

        print(f'{number} is an even number')

    else:

        print(f'{number} is an odd number')

else:

    print("Your input wasn't an integer")

"""
Ask user what hour is it, and then greet the user. 
"""

hour = input('What hour is it? (24h): ')


try:

    if hour.isdigit:

        if int(hour) in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 24]:

            print('Good morning')

        elif int(hour) in [12, 13, 14, 15, 16, 17]:

            print('Good afternoon')

        elif int(hour) in [18, 19, 20, 21, 22, 23]:

            print('Good evening')

        else:

            print('The hour should be an integer number between 0 and 24')

except ValueError:

    print('Type an integer number between 0 and 24')


"""
Ask the user for their first name. If the name has 4 letters or less
say: "Your name is short"; if it has between 5 and 6, say: 
"Your name is normal"; if it has more than 6 characters: "Your name is big". 
"""

nome = input('Tell me your first name: ')

try:

    if len(nome) <= 4:

        print('Your name is short')

    elif len(nome) > 4 and len(nome) < 7:

        print('Your name is normal')

    else:

        print('Your name is big')

except Exception:

    print('Error')
