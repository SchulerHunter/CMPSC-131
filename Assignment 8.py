# This program reads a randomly generated number file
# It then stores all of the numbers in a list
# Finally it returns the numbers, the minimum, the maximum, the sum, and the average

# Author: Hunter Schuler

# Open the file and initialize variables
file = open("random.txt", "r")
nums = []
print("The following values were read from the file:")

# Append the numbers to the list while printing
# For the extra thought, you could have a variable called min and max
# If x is less than min, or greater than max, it will take that variables place
# Then just print those extra variables instead of the min and max functions
for x in file:
    print(x)
    nums.append(int(x))

# Report all values
print("The lowest value on the list is:", min(nums))
print("The max value in the list is:", max(nums))
print("The sum of all values is:", sum(nums))
print("The average of all values is", format(sum(nums)/len(nums), ".1f"))

# Close the file
file.close()
