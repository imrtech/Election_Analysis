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
    print(headers)
    


       

         
    