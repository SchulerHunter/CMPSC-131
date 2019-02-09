# This program accepts a name as an input
# It then checks if that name is a popular boy or girls name
# If it is, it then returns the ranked spot

# Author: Hunter Schuler

# Convert files to lists for easier position tracking
boyList = []
girlList = []
boys = open("BoyNames.txt", "r")
girls = open("GirlNames.txt", "r")
for x in boys:
    boyList.append(x.rstrip())
for x in girls:
    girlList.append(x.rstrip())
boys.close()
girls.close()

# Introduce the program
print("Enter a name to see if it is a popular boy or girl name")

# Receive input and search boy and girl names
while True:
    foundG = False
    foundB = False
    name = input("Enter a name to check, or type 'Stop' to stop: ")
    if name == "Stop" or name == "stop":
        exit(0)
    for x in range(len(girlList)):
        if girlList[x] == name:
            print(name, "is a popular girls name and is ranked:", x + 1)
            foundG = True
    if not foundG:
        print(name, "is not a popular girls name")
    for x in range(len(boyList)):
        if boyList[x] == name:
            print(name, "is a popular boys name and is ranked:", x + 1)
            foundB = True
    if not foundB:
        print(name, "is not a popular boys name")
