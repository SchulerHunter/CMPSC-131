# This program is the same as programming assignment 9
# Except this time it allows for more inputs and creates two functions for variable passing
# It still checks the lists to see of the name is available

# Author: Hunter Schuler


def getNamesList(fileName):
    nameList = []
    file = open(fileName, "r")
    for x in file:
        nameList.append(x.rstrip())
    file.close()
    return nameList


def checkName(testName, nameList):
    i = 0
    for x in getNamesList(nameList):
        i = i + 1
        if testName == x:
            return i
    return 0


# Receive the name as an input then run it through the functions to return the results

print("Enter a name to see if it is a popular girls or boys name")
name = input("Enter a name to check, or 'stop' to stop: ")
while name != "stop":
    if checkName(name, "GirlNames.txt") == 0:
        print(name, "is not a popular girls name")
    else:
        print(name, "is a popular girls name ranked:", checkName(name, "GirlNames.txt"))
    if checkName(name, "BoyNames.txt") == 0:
        print(name, "is not a popular boys name")
    else:
        print(name, "is a popular boys name ranked:", checkName(name, "BoyNames.txt"))
    name = input("Enter a name to check, or 'stop' to stop: ")
