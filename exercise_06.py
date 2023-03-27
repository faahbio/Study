name = input('Write your full name: ')

name_length = len(name)

i = 0

new_name = '*'

while i < name_length:
    letter = name[i]
    print(letter)
    new_name += f'{letter}*'
    
    i += 1

print(new_name)