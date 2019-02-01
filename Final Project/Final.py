# This program retrieves a set of user ID's and their associated sales data
# and returns it in a fashionable manner
# Author: Hunter Schuler


# Reads the salesperson's IDs file and create two Python lists: a list of the IDs and
# A list that is a two dimensional list of the sales data by quarter for each salesperson
def getIDs(filename):
    # Create the lists items and open the file
    id_list = []
    sales_data = []
    file = open(filename, 'r')
    for line in file:
        # Add the ID's for each user and populate the sales_data
        id_list.append(line.rstrip())
        sales_data.append([0.0, 0.0, 0.0, 0.0])
    file.close()
    # Sort the ID list
    id_list.sort()
    return id_list, sales_data


# Reads the sales data file and add all the sales data to the sales_data list totaling all
# The monthly data into the totals for the proper quarter by sales ID
# Only modifies the sales_data list
def process_sales_data(filename, id_list, sales_data):
    file = open(filename, 'r')
    for line in file:
        # Parse the line into three values
        Data = line.split(None, 3)
        # Set the list column to be the ID
        col = id_list.index(Data[0])
        # Convert the months into the quarter
        if Data[1] == '1' or Data[1] == '2' or Data[1] == '3':
            row = 0
        elif Data[1] == '4' or Data[1] == '5' or Data[1] == '6':
            row = 1
        elif Data[1] == '7' or Data[1] == '8' or Data[1] == '9':
            row = 2
        elif Data[1] == '10' or Data[1] == '11' or Data[1] == '12':
            row = 3
        # Add the value into the correct list item
        val = float(Data[2])
        sales_data[col][row] += val
    file.close()


# Print report is to be called when a printed annual report is requested
# Utilizes the id_list and sales_data lists to print report while calculating
# The quarterly sum and determining the max
def print_report(id_list, sales_data):
    # Create space for quarterly totals
    id_list.append("Total")
    sales_data.append([0.0, 0.0, 0.0, 0.0])

    # Calculate quarterly totals
    for i in range(len(sales_data) - 1):
        for j in range(0, 4):  # Only four quarters so this would work for any data set
            sales_data[len(sales_data) - 1][j] += sales_data[i][j]

    # Calculate totals per person + overall
    for i in range(len(sales_data)):
        total = 0
        for j in range(len(sales_data[i])):
            total += sales_data[i][j]
        sales_data[i].append(total)

    # Calculate the max sales by salesperson for a quarter
    maxIDAmount = 0
    for i in range(len(sales_data) - 1):
        for j in range(len(sales_data[i]) - 1):
            if sales_data[i][j] > maxIDAmount:
                maxIDAmount = sales_data[i][j]
                maxID = id_list[i]

    # Calculate the max sales in a quarter
    maxQuarterAmount = 0
    for j in range(len(sales_data[len(sales_data) - 1]) - 1):  # This loops through the totals for each quarter
        if sales_data[len(sales_data) - 1][j] > maxQuarterAmount:
            maxQuarterAmount = sales_data[len(sales_data) - 1][j]
            maxQuarter = str(j + 1)

    print('{:-^55}'.format('Annual Sales Report')+'\n\n')
    print('{:<5s}{:>10s}{:>10s}{:>10s}{:>10s}{:>10s}'.format('ID', 'QT1', 'QT2', 'QT3', 'QT4', 'Total'))
    for i in range(len(sales_data)):
        print('\n' + '{:<5s}'.format(id_list[i]), end="")
        for j in range(len(sales_data[i])):
            print('{:>10s}'.format(str(format(sales_data[i][j], '.2f'))), end="")
    print('\n')
    print('Max sales by Salesperson: ID =', maxID + ', Amount = $' + format(maxIDAmount, '.2f'))
    print('Max sales by Quarter: Quarter =', maxQuarter + ', Amount = $' + format(maxQuarterAmount, '.2f'))


# The main function controls the flow of the program
def main():
    IDDataFile = input("Enter the name of the sales ID File: ")
    id_list, sales_data = getIDs(IDDataFile)
    SalesDataFile = input("Enter the name of the sales Data File: ")
    process_sales_data(SalesDataFile, id_list, sales_data)
    print_report(id_list, sales_data)


main()
