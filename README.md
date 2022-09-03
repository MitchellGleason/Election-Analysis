# Election Analysis
  
 ## Challenge Overview
 The purpose of this election audit analysis was to read the given data file and calculate: total number of votes, the complete list of candidates, total number of votes per candidate, percentage of votes that each candidate won, determine the winner of the election based on popular vote, determine the number of votes per county and their percentage of the total vote, and finally, determine the county with the largest voter turnout.
 
 ## Election-Audit Results
 The analysis of the election shows that:
 - There were 396,711 votes cast in the election
 - The county results were:
   - Jefferson was 10.5% of the vote and had 38,855 votes
   - Denver was 82.8% of the vote and had 306,055 votes
   - Arapahoe was 6.7% of the vote and had 24,801 votes
- The county with the largest voter turnout was:
   - Denver, with 82.8% of the vote and 306,055 votes
- The candidate results were:
   - Charles Casper Stockham received 23.0% of the vote and 85,213 votes
   - Diana DeGette received 73.8% of the vote and 272,892 votes
   - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes
 - The winner of the election was:
   - Diana DeGette, who received 73.8% of the vote and 272,892 votes
   
 Shown in the file .txt as:
 
 ![Capture](https://user-images.githubusercontent.com/111290810/188290899-1583f2d1-0735-4450-acf7-fdc990c44496.PNG)

## Election-Audit Summary
The provided python script is certainly able to be used for any given election only if certain variables stay the same. The voter data must be provided in a .csv file format, and must contain the columns in this exact order: Ballot ID, County, Candidate. This is because the script uses the specific indexes of these columns, assuming that each column is static, as seen here:
```
/# For each row in the CSV file.
for row in reader:

   /# Add to the total vote count
   total_votes = total_votes + 1

   /# Get the candidate name from each row.
   candidate_name = row[2]

   /# 3: Extract the county name from each row.
   county_name = row[1]
```
Additionally, the .csv must be in the same file directory as the script, and must be within a folder named 'Resources', and a folder named 'Analysis' must be created in the same file directory, as seen here:
```
/# Add our dependencies.
import csv
import os

/# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
/# Add a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")
```
Modifications in this code can be made for a different file path and for a different column order in the .csv file.

There are also further modifications and additions that can be made to this code to better suit other elections. The ballot IDs can be checked against a separate, more secure file, in order to ensure that they are all valid. The ballot IDs could also be checked against other IDs in this file to ensure there are no duplicates. Another addition could be the determination of the voter turnout (both total and per county) as a percentage of the total voter eligible population. Additionally, a section can be added to determine that number of votes that each candidate received in each county in order to better determine the candidates popularity in different areas.

## Resources
 - Data source: election_results.csv
 - Software: Python 3.9.12, Visual Code Studio 1.71.0
