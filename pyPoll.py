# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winer of the election based on popular vote.

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources/election_results.csv")

# To write a file to a directory on computer do the below.
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize variable that will increment by 1 as we read each row in the for loop. Called an accumulator. Line 63 prompts this step.
total_votes = 0

# Declare new list for candidate options. Line 72 prompts this step.
candidate_options = []

# Declare new dictionary for candidate votes.
candidate_votes = {}

# Declare variable for empty string for winning candidate.
# Declare a variable for the "winning count" equal to zero.
# Declare a variable for the "winning_percentage" equal to zero.
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    
#      # Print file object.
#      print(election_data)

# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

# Use the open statement to open the file as a text file.
#outfile = open(file_to_save, "w")

# Write some data to the file.
#outfile.write("Hello World")

# Close the file
#outfile.close()

# To make code cleaner use with statement instead of open() and close().
    # with open(file_to_save, "w") as txt_file:
     #txt_file.write("Hello World you rule")
     
     # Write three counties to the file.
     #txt_file.write("Arapahoe, Denver, Jefferson")

     # To write counties on separate lines add the new line escape sequence \n.
     #txt_file.write("Arapahoe\nDenver\nJefferson")

     # Add more lines before counties and use \n.
    #  txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")

    # to do: read and analyze the data here.
     # Read the file object with the reader function. This will aloow us to read CSV file using csv module with the reader function.
    file_reader = csv.reader(election_data)
    
    # To iterate through file_reader variable and print row, header and column names add row statement.
    # for row in file_reader:
    #     print(row)

    # Print the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
    # Initialize accumulator variable above the with open() statement on line 22.

      # 2. Add the total vote count.  
        total_votes += 1
      
      # Print the candidate name from each row.
        candidate_name = row[2]
      
      # Add the candidate_name to the candidate _options list using the append() method.
        # candidate_options.append(candidate_name)

      # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            
            # Add it to the list of candidates. Add the candidate_name to the candidate _options list using the append() method.
            candidate_options.append(candidate_name)

            # Create each candidate as a key.
            candidate_votes[candidate_name] = 0

            # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Print the candidate list.
# print(candidate_options)

# Print the candidate vote dictionary.
# print(candidate_votes)
    
#3. Print the total votes
# print(total_votes)

# Declare a new list before the with open() statement to add candidate_options.
# Declare a new dictionary at line 25 for candidate votes.
    
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    
    # 2. Retreive vote count of a candidate.
    votes = candidate_votes[candidate_name]
    
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) /float(total_votes) * 100

    # 4. Print the candidate name and percentage of votes.
    # print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

  #  To do: print out each candidate's name, vote count, and percentage of
  # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    
  # Determine winning vote count and candidate
  # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
      # 2. If true then set winning_count = votes and winning_percent =
      # vote_percentage.
      winning_count = votes
      winning_percentage = vote_percentage
       # 3. Set the winning_candidate equal to the candidate's name.
      winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

#  To do: print out the winning candidate, vote count and percentage to
#   terminal.

       

         
    