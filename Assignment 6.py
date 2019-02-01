# This program writes a number of random numbers
# The number of random numbers is decided by the user from an input
# The output is printed to a text file called random.txt

# Author: Hunter Schuler

# Import necessary libraries
import random

#  First prompt the user for the number of inputs, create the file
file = open("random.txt", "w")
numberOfEntries = int(input("How many numbers would you like to write? "))

# Fill the file with random numbers
for x in range(numberOfEntries):
    file.write(str(random.randint(1, 500)) + "\n")

# Proper code etiquette is to always close a file afterwards
file.close()
