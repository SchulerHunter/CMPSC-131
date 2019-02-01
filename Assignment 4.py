# This program uses a while loop to continuously prompt the user to input grades
# Once the user is done inputting grades, they finish with a negative number
# The program then returns the average

# Author: Hunter Schuler

# Initialize variables
# Create the loop to request for the grades
gradeIn = float(input("Enter a test score, -1 to get the average: "))
grades = []
totGrades = 0
while gradeIn >= 0:
    grades.append(gradeIn)
    gradeIn = float(input("Enter a test score, -1 to get the average: "))

# Determine the total
for x in grades:
    totGrades += x

# Print the average
print("The average for all the grades is:", totGrades / len(grades))
