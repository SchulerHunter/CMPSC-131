# This program reads the numbers from assignment 6
# It then prints them out, along with a count

# Author: Hunter Schuler

# First set the file to be read and initialize variable
file = open("random.txt", "r")
total = 0
count = 0
print("The following numbers were read from the file random.txt:")

# Loop through the file and print the numbers while calculating sum and count
for x in file:
    print(x)
    total += int(x)
    count += 1

# Print the sum and count
print("There were", str(count), "numbers in the file with a sum of", str(total))

# Close the file to maintain etiquette
file.close()
