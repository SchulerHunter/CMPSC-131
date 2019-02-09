# This program uses a while loop to continuously prompt the user to input grades
# Once the user is done inputting grades, they finish with a negative number
# The program then returns the average

# Author: Hunter Schuler

# Initialize variables
grades = []
gradeIn = 0
totGrades = 0

# Create the loop to request for the grades
while gradeIn >= 0:
    gradeIn = input("Enter a test score or a negative to receive the average: ")
    try:
        gradeIn = float(gradeIn)
        if gradeIn > 0:
            grades.append(gradeIn)
            totGrades += gradeIn
    except ValueError:
        print("What you entered was not a number, try again")
        gradeIn = 0

if len(grades) == 0:
    print("You did not enter any numbers to average")
else:
    print("The sum of the grades is:", totGrades)
    print("The average of the grades is:", totGrades/len(grades))
