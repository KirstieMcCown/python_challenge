# Import os module 
import os 

# Import csv module 
import csv

# Set file path
budget_csv = os.path.join("Resources", "budget_data.csv")

# Set a variable for the net total amount of "Profit/Losses" over the entire period
total_p_l = 0.00

 # Set a variable for the total number of months included in the dataset (exclude header row)
total_months = 0

# Create empty lists to hold the profit increase, decrease and associated dates
profit = []
month = []


# Open and read csv file 
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Read the header row first and print to check that we have read the data correctly
    csv_header = next(csvfile)
    # print(f"Header: {csv_header}")
    
    # Read through each row of data after the header
    for row in csvreader:
        # Add total months 
        total_months = int(total_months+1)

# Print to check total months is being calculated correctly
# print(total_months)

        # Add profit amount to the total 
        total_p_l = (float(row[1]) + total_p_l)
       
# Print to check total profit/loss is being calculated correctly
# print(total_p_l)     

        # Calculate the average of the changes in "Profit/Losses" over the entire period
        average_change = (total_p_l/total_months)

# Print to check average change is being calculated correctly
# print(average_change)

        # Find greatest increase or decrease in profits (amount) over the entire period
        profit.append(float(row[1]))

        # Store a variable for max profit
        max_profit = (max(profit))
        # print(max_profit)

        # Store a variable for min profit
        min_profit = (min(profit))
        # print(min_profit)

        # Set a variable for the increase/decrease date
        max_date = str(row[0])
        # print(date)

        min_date = str(row[0]) 

        # Find date of the greatest increase in profits over the entire period
        if row[1] == (max(profit)):
                max_date = str(row[0])

        if row[1] == (min(profit)):
                min_date = str(row[0])


# Print the analysis to the terminal and export a text file with the results

# Print Header
print("Financial Analysis")
print("----------------------------")

# Print total number of months
print(f"Total Months: {total_months} months")

# Print net total profit/loss  
print(f"Total: ${total_p_l:.0f}")

# Print average change in profit/loss
print(f"Average Change: ${average_change:.2f}")

# Print Greatest Profit Increase and Corresponding Date 
print(f"Greatest Increase in Profits: {max_date} (${max(profit):.2f})")

# Print Greatest Profit Decrease and Corresponding Date
print(f"Greatest Decrease in Profits: {min_date} (${min(profit):.2f})")