#The data we need to retrieve
#1. The total numebr of votes cast
#2 A complete list of candidates who received votes
#3 The percentage of votes each candidate won
#4 The total number of votes each candidate won
# The winner of the election based on popular vote
# Import the datetime class from the datetime module.
from platform import python_branch
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize total votes variable
total_votes = 0

# Initalize candidate options variable
candidate_options = []

#Initialize candidate votes dictionary
candidate_votes = {}

# Initialize winning candidate variable
winning_candidate = ""

# Initialize winning count variable
winning_count = 0

# Initialize winning percentage variable 
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    #Print the header row.
    headers = next(file_reader)
    #print(headers)

    #Print each row in the CSV file
    for row in file_reader:
            #to print all rows if need - print(row)
            # Add to the total vote count
            total_votes += 1
            # Print the candidate name from each row
            candidate_name = row[2]


            # Setting if statement to see if candidate name is already in candidate options list
            if candidate_name not in candidate_options:

            # Adding candidate_name to the candidate_options list created
                candidate_options.append(candidate_name)

            # Begin teacking that candidate's vote count
                candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
            candidate_votes[candidate_name] += 1   
        # Saving results to text file
    with open(file_to_save, "w") as txt_file:
        # Election results and Total Votes heading
        election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
        print(election_results, end="")
    # Save the final vote count to the text file.
        txt_file.write(election_results)
        # 1. Iterate through the candidate list.        
        for candidate_name in candidate_votes:
            # 2. Retrieve the vote count of a candidate
            votes = candidate_votes[candidate_name]
            # 3. Calculate the percentage of votes
            vote_percentage = float(votes) / float(total_votes) * 100
            # Print the candidate name and percentage of votes
            #print(f"{candidate_name}: receieved {vote_percentage:.1f}% of the vote.")

            #Set candidate results variable to include candidate name, voting percentage, and number of votes
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            #Print each candidate, their voter count, and percentage to the terminal
            print(candidate_results)

            #Save the candidate results to the text file
            txt_file.write(candidate_results)

            # Determine winning vote count and candidate
            # 1. Determine if the votes are greater than the winning count
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If the statement is true, then set winning_counts = votes and winning_percentage = vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage
                # 3. Set the winning_candidate equal to the candidate's name
                winning_candidate = candidate_name
        #Print out the winning candidate summary
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        print(winning_candidate_summary)

        #Save the winning candidate's name to the text file
        txt_file.write(winning_candidate_summary)


    #Print out the candidate options
    #print(candidate_options)

    #Print the candiate vote dictionary
    #print(candidate_votes)


    