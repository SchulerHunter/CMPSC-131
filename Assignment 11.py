# This program prompts the user to input a calculate the temperature in fahrenheit and the wind speed
# It then returns the wind chill and asks if the user would like to find another wind chill

# Author: Hunter Schuler


def windchill(temp, speed):
    return 35.74 + .6215 * temp - 35.75 * speed**.16 + .4275 * temp * speed**.16


# Prompt the user for the temperature and speed, then pass it to the function to return windchill
print("This program accepts the temperature in fahrenheit and speed of the wind to calculate the windchill factor")
cont = 'y'
while cont == 'y':
    temp = int(input("Please input the temperature in Fahrenheit: "))
    speed = int(input("Please input the speed in miles per hour: "))
    print("The windchill is:", format(windchill(temp, speed), '.1f'))
    cont = input("Enter 'y' if you would like to find another windchill, otherwise anything else to exit ")
