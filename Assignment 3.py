# This program prompts the user for how many $100 packages they would like to order
# It then add a discount according to the following table and prints the total cost
# 0-9 | No discount
# 10 - 19 | 10% discount
# 20-49 | 20% discount
# 50 - 99 | 30% discount
# 100+ | 40% discount

# Author: Hunter Schuler

# Ask for how many items they would want to order and calculate the total
orderQty = int(input("How many items would you like to order? "))
total = orderQty * 100

# Determine the discount amount based on the quantity
discount = 0
if orderQty >= 100:
    discount = .4 * total  # 40% = .4
elif orderQty >= 50:
    discount = .3 * total  # 30% = .3
elif orderQty >= 20:
    discount = .2 * total  # 20% = .2
elif orderQty >= 10:
    discount = .1 * total  # 10% = .1

# Recalculate the total
total -= discount

# Print the total and the discount amount
print("The total cost will be $" + format(total, '.2f'), "with a discount of $" + format(discount, '.2f'))
