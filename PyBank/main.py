import os
import csv

# Path to the budget data CSV file
PyBank_csv = os.path.join("Resources","budget_data.csv")

# Open the input file and read in the data
with open(PyBank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skip header row
    header = next(csvreader)

    # Initialize variables
    number_of_months = 0
    net_total_amount = 0
    p_l = []
    date = []
    
    # Loop through rows in the csv file
    for row in csvreader:
        # Count the number of months
        number_of_months += 1
         # Calculate the net total amount of profit/loss
        net_total_amount += int(row[1])
        # Create a list of profit/loss values and a list of dates
        p_l.append(row[1])
        date.append(row[0])

    # Create a list of changes in profit/loss for each month
    changes = [0]
    for i in range(len(p_l) - 1 ):
        changes.append(int(p_l[i+1]) - int(p_l[i]))
    
    # Find the greatest increase and greatest decrease in profit/loss
    greatest_increase = round(max(changes),0)
    greatest_increase_index = changes.index(greatest_increase)
    greatest_increase_date = date[int(greatest_increase_index)]

    greatest_decrease = round(min(changes),0)
    greatest_decrease_index = changes.index(greatest_decrease)
    greatest_decrease_date = date[int(greatest_decrease_index)]

    # Print results to the terminal
    print("Financial Analysis")
    print("-------------------------------------")
    print(f'Total Months: {number_of_months}')
    print(f'Total: ${net_total_amount}')
    print(f'Average Change: ${round((sum(changes) / (len(changes) - 1)), 2)}')
    print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})')   
    print(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})')

# Write results to a text file     
with open("budget_results.txt", 'w') as txtfile:
    txtfile.write(f'Financial Analysis\n')
    txtfile.write(f'-------------------------------------\n')
    txtfile.write(f'Total Months: {number_of_months}\n')
    txtfile.write(f'Total: ${net_total_amount}\n')
    txtfile.write(f'Average Change: ${round((sum(changes) / (len(changes) - 1)), 2)}\n')
    txtfile.write(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n')
    txtfile.write(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n')
