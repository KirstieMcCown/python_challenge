# Import os module 
import os 

# Import csv module 
import csv

# Set file path
election_csv = os.path.join("Resources", "election_data.csv")

# Set a variable for the total amount of votes in the dataset (exclude header row)
total_votes = 0

candidate_votes = 0

# Create an empty list to hold the list of candidates
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
# print(total_votes)

# Append the candidates into the list
        candidates.append(row[2])

# Create a set with only unique candidate values 
unique_candidates = set(candidates)
# print(len(unique_candidates))
# print(unique_candidates)
        
# Calculate total votes per candidate 
if (row[2]) == "Khan":
    candidate_votes = candidate_votes +1 
print(candidate_votes)

# print the analysis to the terminal and export a text file with the results

# Print Header
print("Election Results")
print("----------------------------")

# Print total number of votes
print(f"Total Votes: {total_votes}")
print("----------------------------")

# Print total number and percentage of votes per candidate
for names in unique_candidates:
    print(names) 
# 
#
#
# print("----------------------------")

# Print the winner of the election
# print(f"Winner: {}")
# print("----------------------------")