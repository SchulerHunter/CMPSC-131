#  This program prompts the user to enter a number
#  It then prompts for number from 0 to that number
#  Ultimately it figures out which digit was not entered

#  Author: Hunter Schuler

#  Prompt for a number, calculate the summation factorial, initialize the total
number = int(input("Please enter a number: "))
summation = (number*(number+1))/2
total = 0

#  Prompt for sub-sequent numbers
for x in range(number - 1):
    digit = int(input("Please enter a number between 0 and " + str(number) + ": "))
    while digit > number or digit < 0:
        print("Item entered not in range")
        digit = int(input("Please enter a number between 0 and " + str(number) + ": "))
    total += digit

#  Calculate the missing number
print("The missing number is: " + str(int(summation - total)))
