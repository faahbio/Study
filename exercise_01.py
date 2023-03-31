import os

name = input("What's your name: ")
nickname = input("Tell me your nickname: ")
age = int(input("What's your age: "))
height_meters = float(input("How tall are you: "))

os.system('cls')

print(f'Your name is {name}')
print(f'Your nickname is {nickname}')
print(f"You're {age} years old")

if age >= 18:

    print("You can drink and drive")

else:

    print("You're too young to drink and drive")

if height_meters <= 1.60:

    print("You're small")

elif (height_meters > 1.60) and (height_meters <= 1.80):

    print("You have an average height")

else:

    print("You are really tall")
