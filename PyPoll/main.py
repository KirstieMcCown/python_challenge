# Import os module 
import os 

# Import csv module 
import csv

# Set file path
election_csv = os.path.join("Resources", "election_data.csv")

# Set a variable for the total amount of votes in the dataset (exclude header row)
total_votes = 0
candidate_votes = 0
percentage = 0
NumberVotes = 0
WinnerCount = 0

# Create an empty list to hold the list of candidates
candidates = []
votecount = []
votepercentage = []

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

# Transfer names in the set, back to a list to be able to be called upon 
unique_candidates = list(unique_candidates)

# Print the length of the list unique_candidates (this shows how many unique candidates there are)
# print(len(unique_candidates))

# Print the names of all unique candidates
# print(unique_candidates)

# Print each name (item) in the list unique_candidates
# print(unique_candidates[0])
# print(unique_candidates[1])
# print(unique_candidates[2])
# print(unique_candidates[3])
        
# Calculate total votes per candidate 
for votes in range(0,len(unique_candidates)):
    candidate_votes = candidates.count((unique_candidates[votes]))

# Append votes per candidate into a list 
    votecount.append(candidate_votes)

# print(unique_candidates[0])
# print(candidate_votes)

# Calculate percentage of votes per candidate
    percentage = float(round((candidate_votes/total_votes)*100,2))

# Append percentage of votes per candidate into a list 
    votepercentage.append(percentage)

# print(percentage)

# Calculate the winner by looping through the unique candidate list
for name in range(len(unique_candidates)):

    if WinnerCount < votecount[name]:
        Winner = unique_candidates[name]
        WinnerCount = votecount[name]

# print(Winner)
# print(WinnerCount)

# Print the analysis to the terminal

# Print Header
print("Election Results")
print("----------------------------")

# Print total number of votes
print(f"Total Votes: {total_votes}")
print("----------------------------")

# Print total number and percentage of votes per candidate
for i in range(len(unique_candidates)):
    print(f"{unique_candidates[i]}: {votepercentage[i]:.3f}% ({votecount[i]})")
print("----------------------------")

# Print the winner of the election
print(f"Winner: {Winner}")
print("----------------------------")


# Export a text file with the results

# Specify the file to write to
output_path = os.path.join("Analysis", "Election_Results.csv")

# Open the file using "write mode."
with open(output_path, 'w', newline="") as csvfile:

        # Initialise csv.writer
        csvwriter = csv.writer(csvfile, delimiter=",")

        # Write the first row
        csvwriter.writerow(["Election Results"])

        # Write rows 2 to 7
        csvwriter.writerow(["----------------------------"])
        csvwriter.writerow([f"Total Votes: {total_votes}"])
        csvwriter.writerow(["----------------------------"])
        for i in range(len(unique_candidates)):
            csvwriter.writerow([f"{unique_candidates[i]}: {votepercentage[i]:.3f}% ({votecount[i]})"])
        csvwriter.writerow(["----------------------------"])
        csvwriter.writerow([f"Winner: {Winner}"])
        csvwriter.writerow(["----------------------------"])



