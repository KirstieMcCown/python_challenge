# Import os module 
import os 

# Import csv module 
import csv

# Set file path
election_csv = os.path.join("Resources", "election_data.csv")

# Set a variable for the net total amount of votes in the dataset (exclude header row)
total_votes = 0

# Create empty lists to hold the list of candidates
candidates = []

# Open and read csv file 
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Read the header row first and print to check that we have read the data correctly
    csv_header = next(csvfile)
    # print(f"Header: {csv_header}")
    
    # Read through each row of data after the header
    for row in csvreader:
        # Add total months 
        total_votes = int(total_votes+1)

# Print to check total votes is being calculated correctly
print(total_votes)

        # Append the candidates into the list
        candidates.append(row[2])
          
        # Create a set with only unique candidate values 
        unique_candidates = set(candidates)

print(unique_candidates)
        
        # profit_increase.append(float(row[1]))
        # profit_increase.sort()
        # profit_increase = profit_increase[-1]
        # print(profit_increase)

        # profit_i_month.append(str(row[0]))
        # print(max(profit_i_month))

        # Find greatest decrease in profits (date and amount) over the entire period
        # profit_decrease
        # profit_d_month

# print the analysis to the terminal and export a text file with the results

# Print Header
print("Election Results")
print("----------------------------")

# Print total number of votes
print(f"Total Votes: {total_votes}")
print("----------------------------")

# # # Print net total profit/loss  
# # print(f"Total: ${total_p_l:.0f}")

# # # Print average change in profit/loss
# # print(f"Average Change: ${average_change:.2f}")

# # # print(f"Greatest Increase in Profits: {profit_i_month} {profit_increase:.2f}")
# # # # print(f"Greatest Decrease in Profits: {profit_d_month} "({profit_decrease:.2f})""