import math
# This program uses the idea of the Sieve of Eratosthenes
# To calculate all of the prime numbers on an array from 2 to 999
# If you wanted, you could change all 1000's to a variable input called n
# And calculated from 2 to n where n is a real number

# Author: Hunter Schuler

# First initialize the array to all 1
values = []
results = []
for x in range(1000):
    values.append(1)

# Change values 0 and 1 to false
values[0] = 0
values[1] = 0

# Following the logic of the sieve, change all applicable values to false
for x in range(2, int(math.sqrt(1000))):
    if values[x] == 1:
        for y in range(1000):
            if x*x + y*x < 1000:
                values[x*x + y*x] = 0

# Store all values in a second list
for x in range(len(values)):
    if values[x] == 1:
        results.append(x)

# Print the second list
print("The prime numbers from 2 to 999 as determined by the Sieve of Eratosthenes are:")
for x in range(0, len(results), 10):
    print(results[x:x+10])
