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


        # Set a vairable to return the month relating to the greatest increase or decrease
        # profit_i_month = (row[0])

# # Set a vairable to return the month relating to the greatest decrease
# profit_d_month = 

        # Set a variable for greatest increase in profits (date and amount) over the entire period
        profit_increase = (float(row[1]))
        print(profit_increase)

# # Set a variable for greatest decrease in losses (date and amount) over the entire period
# profit_decrease = 

# print the analysis to the terminal and export a text file with the results

# # Print Header
# print("Financial Analysis")
# print("----------------------------")

# # Print total number of months
# print(f"Total Months: {total_months} months")

# # Print net total profit/loss  
# print(f"Total: ${total_p_l:.0f}")

# # Print average change in profit/loss
# print(f"Average Change: ${average_change:.2f}")


# # print(f"Greatest Increase in Profits: {profit_i_month} {profit_increase:.2f}")
# # print(f"Greatest Decrease in Profits: {profit_d_month} "({profit_decrease:.2f})"")