import os

word = 'basel'

guessed_letters = ''

tries = 0

while True:

    letter = input('Type a letter: ')

    if len(letter) > 1:

        print('Type only one letter!')
        continue

    if letter in guessed_letters:

        print(f"You've already guessed this letters: {guessed_letters}!")
        continue

    if letter in word:

        guessed_letters += letter
        tries += 1

    else:

        tries += 1

    new_word = ''
    for letter in word:

        if letter in guessed_letters:

            new_word += letter

        else:

            new_word += '*'

    print(new_word)

    if new_word == word:

        os.system('cls')
        print('Congrats! You nailed it!!!')
        print(f'You used {tries} tries!')
        print(f'The word was {new_word}')
        guessed_letters = ''
        tries = 0
