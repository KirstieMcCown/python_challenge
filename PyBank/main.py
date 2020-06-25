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

# Set a variable for max profit, min profit and associated months 
max_profit = 0
max_profit_month = ""

min_profit = 0
min_profit_month = ""

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
# 
        # Calculate the average of the changes in "Profit/Losses" over the entire period
        # change = (max_profit - min_profit)
        average_change = (total_p_l/total_months)

# Print to check average change is being calculated correctly
# print(average_change)

        # Find greatest increase or decrease in profits (amount) over the entire period
        profit.append(float(row[1]))

        # Find greatest increase or decrease in profits (month) over the entire period
        month.append(str(row[0]))

# Assign new values for min and max profit variables

        max_profit = (max(profit))
        min_profit = (min(profit))

# print(max_profit)
# print(min_profit)

# Find max profit and max profit date
        if float(row[1]) == (max(profit)):
                max_profit_month = (row[0])

# Print max profit month to check date is correct
# print(max_profit_month)

# Find max profit and max profit date
        if float(row[1]) == min(profit):
                min_profit_month =  row[0]

# Print max profit month to check date is correct
# print(min_profit_month)


# Print the analysis to the terminal

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
print(f"Greatest Increase in Profits: {max_profit_month} (${max_profit:.2f})")

# Print Greatest Profit Decrease and Corresponding Date
print(f"Greatest Decrease in Profits: {min_profit_month} (${min_profit:.2f})")

# Export a text file with the results
# output_path = os.path.join("..", "Analysis", "Financial_Analysis.csv")

# with open (output_path, "w", newline-"") as csvfile:
#         csvwriter.writerow("Financial Analysis")
#         csvwriter.writerow("----------------------------")
#         csvwrite.writerow(f"Total Months: {total_months} months")
#         csvwrite.writerow(f"Total: ${total_p_l:.0f}")
#         csvwrite.writerow(f"Average Change: ${average_change:.2f}")
#         csvwrite.writerow(f"Greatest Increase in Profits: {max_date} (${max(profit):.2f})")
#         csvwrite.writerow(f"Greatest Decrease in Profits: {min_date} (${min(profit):.2f})")




