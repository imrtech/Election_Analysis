# Election_Analysis

## Project Overview
A Colorado board of elections employee has asked for an election audit to determine the winning candidate, and the county with the largest voter turnout. To perform this analysis we would have to look at the following data:
- The total number of votes cast.
- A list of all the candidates.
- The total number of votes each candidate received.
- The percentage of votes for each candidate
- The winner of the election based on the popular vote
- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout.

## Election Audit Results
Based on the analysis performed on the election data, the following information was found:
 - A total of 369,711 votes were cast in this election.
 - The counties represented were Arapahoe, Denver and Jefferson.
 - Denver county had 82.8% of the popular vote, with 306,055 total votes.
 - Jefferson county had 10.5% of the popular vote, with 38,855 total votes.
 - Arapahoe county had 6.7% of the popular vote, with 24,801 total votes.
 - Denver county had the largest number of votes and voter turnout with 82.8% of the popular vote.
 
 ![This is an image](/Resources/Election_Results_by_county_vote.png)
 
 - The candidates were Charles Casper Stockham, Diana DeGette, and Raymon Anthony Doane.
 - Charles Casper Stockham received 23.0% of the vote with 85,213 number of votes.
 - Diana DeGette received 73.8% of the vote with 272,892 number of votes.
 - Raymon Anthony Doane received 3.1% of the vote with 11,606 number of votes.
 - The winner of the election is Diana DeGette with 73.8% of the total vote and 272,892 total number of votes.

  ![This is an image](/Resources/Election_Results_by_candidate.png)

- Here is the link to the election analysis.txt file: [filename](/analysis/election_analysis.txt)
- Here is the link to the election results.csv file: [filename](/Resources/election_results.csv)
- The py code file can be found here:  [filename](/PyPoll_Challenge.py)

Here is the code used to find the total number of votes:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

Here is the code used to find the county with the highest number of votes":

        if (county_vote > largest_county_turnout_count) and (county_vote_percentage > largest_county_percentage):
            largest_county_turnout_count = county_vote
            largest_county_turnout = county
            largest_county_percentage = county_vote_percentage

    largest_county_turnout_print = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"-------------------------\n")
    print(largest_county_turnout_print)   

Here is the code to find the winning candidate:

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)



## Election Audit Summary
To run the analysis on the data source, election_results.csv, we used Python version 3.10.8, Visual Studio Code version 1.72.2, and Git Bash version 2.38.1 Windows.1. The code developed during this analysis is structured, orderly and customizable, making it useful for future analysis on other election results. The dataset contains three headers, the Ballot ID, County and Candidate Name which made it possible to find the total number of votes, assuming they are all unique votes, the county with the largest number of votes and the winner. The county with the largest number of votes is particularly useful information, and can lead to other kinds of analysis about high voter turnout. For example, we can look at the number of eligible voters who participated in the elections. We generally want to see this numbers go up. Additionally, the code can be updated to include analysis on the total number of votes each candidate received by county.  This would be useful campaign information. 

  ![This is an image](/Resources/countyvotesbycandidate.png)

Additional regions could be used instead of counties, such as city or state, without having to modify the code that much. This code would be helpful in analyzing other data similar to this.

  ![This is an image](/Resources/capturing_other_election_data1.png)



