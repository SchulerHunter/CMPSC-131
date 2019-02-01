# This program prompts the user for a number of sides
# Then uses turtle graphics to draw the shape with the number of sides

# Author: Hunter Schuler

# Define the used libraries
import turtle
import random

# Specify the colors list to choose the line color and fill color.
colors = ['coral', 'gold', 'brown', 'red', 'green', 'blue', 'yellow',
          'purple', 'orange', 'cyan', 'pink', 'magenta', 'goldenrod']

# Define both the window and the pen to use with the turtle functions
pen = turtle.Turtle()
pen.shape("turtle")

# The makePolygon function draws a polygon with the number of sides,
# side length, border color, border width, and fill color as specified.


def makePolygon(sides, length, borderColor, width, fillColor):
    angle = 360/sides
    pen.reset()
    pen.showturtle()
    pen.width(width)
    pen.color(borderColor, fillColor)
    pen.begin_fill()
    for i in range(0, sides):
        pen.forward(length)
        pen.right(angle)
    pen.end_fill()


# A while loop to prompt the user to enter the number of sides they wish
# to have displayed in their shape, while also calculating colors and width
userSides = int(input("Enter the number of sides, less than 3 to exit: "))
while userSides >= 3:
    sideLength = 600/userSides
    outColor = colors[random.randint(0, 12)]
    lineWidth = (userSides % 20) + 1
    inColor = colors[random.randint(0, 12)]
    makePolygon(userSides, sideLength, outColor, lineWidth, inColor)
    userSides = int(input("Enter the number of sides, less than 3 to exit: "))

print("Thank you for using the polygon generator tool.")
