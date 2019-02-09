# This program receives an input from the user and prints
# The temperature in Celsius with it's Fahrenheit conversion
# From 0 to the input

# Author: Hunter Schuler

# Receive an input from the user
maxTemp = int(input("Enter the number celsius temperatures to display: "))
print("Celsius\tFahrenheit")
for x in range(maxTemp + 1):
    print(x, '\t\t', format((9/5)*x + 32, '.1f'))
