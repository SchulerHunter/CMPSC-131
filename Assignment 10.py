# This program prompts the user for the amount of time an object will fall
# Then, using physical kinematics calculates how far the object will fall

# Author: Hunter Schuler


def fallingDistance(time):
    """"This returns the distance an object would fall after the time provided"""
    return .5*9.81*time**2


# Prompt the user to enter a time for an object to fall
print("This program tells you how far an object will fall after so many seconds")
time = int(input("Please enter a time for an object to fall for, or enter a negative to end the program: "))
while time > 0:
    print("An object would fall", fallingDistance(time), "after", time, "seconds pass")
    time = int(input("Please enter a time for an object to fall for, or enter a negative to end the program: "))
