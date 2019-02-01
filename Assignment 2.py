# This program accepts an input of weight in pounds and height in inches
# The program then outputs the user's BMI and tells them the status of their weight

# Author: Hunter Schuler

# Accept an input of the users height and weight
weight = float(input("Please enter your weight in pounds: "))
height = float(input("Please enter your height in inches: "))

# Calculates the BMI and outputs it
BMI = weight * 703 / height**2
print("Your BMI is: " + str(BMI))

# Determines the health of the user
if BMI > 25:
    print("Your BMI indicates that you are overweight.")
elif BMI > 18:
    print("Your BMI indicates that you are optimal weight.")
else:
    print("Your BMI indicates that you are underweight.")
