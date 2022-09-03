#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

#Import dependencies
from calendar import c
import csv
import os
import winsound

#Assign a variable to load the file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Variable to store total number of votes
total_votes = 0

#List with candidate names
candidate_options = []

#Empty dictionary to store candidate names as keys and their total votes as values
candidate_votes = {}

#Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the voting data file and read the file
with open(file_to_load) as election_data:

    #Read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)

    #print each row in the CSV file
    for row in file_reader:
        #Add the total vote count
        total_votes += 1

        #Store each rows candidate name in variable to use in if statement
        candidate_name = row[2]

        #If the candidate does not match any existing index
        if candidate_name not in candidate_options:
            #Add candidate name to the list of options
            candidate_options.append(candidate_name)

            #Begin tracking candidate vote count, initialize at 0
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#Determine the percentage of votes for each candidate by looping through the counts
#Iterate through the candidate list
for candidate_name in candidate_votes:
    #Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]

    #Calculate the percentage of votes
    vote_percentage = votes / total_votes * 100

    #Print the candidate name and percentage of votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #Determine winning vote count and candidate
    #Determine if the votes are greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #If true, set winning_count = votes and winning_percent = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
            
        #Set the winning_candidate = candidate_name
        winning_candidate = candidate_name

#Print winning candidate name, vote count and vote percentage
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

print(winning_candidate_summary)

    