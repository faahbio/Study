name = input("What's your name: ")
height_meters = float(input("Tell me your height in meters: "))
weight_kg = float(input("And how much do you weight (in kg): "))
bmi = weight_kg / (height_meters * height_meters)

print(f"{name}, your BMI is: {bmi:.2f}")