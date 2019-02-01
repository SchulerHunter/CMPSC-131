# This program returns various results from students who participate in sports

# Author: Hunter Schuler

# Create two sets.
baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

# Print the results for each category
print("The students who play baseball are:")
print(baseball)

print("The students who play basketball are:")
print(basketball)

print("The students who play both baseball and basketball are:")
print(baseball.intersection(basketball))

print("The students who play either baseball or basketball are:")
print(baseball.union(basketball))

print("The students who play baseball, but not basketball are:")
print(baseball.difference(basketball))

print("The students who play basketball, but not baseball are:")
print(basketball.difference(baseball))

print("The students who play one sport, but not both are:")
print(baseball.symmetric_difference(basketball))