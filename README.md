# Election_Analysis
## Overview of Election Audit
### Purpose
A request was submitted by a Colorado election commission committee to provide an election analysis on a US congressional precinct in Colorado. More specifically, it was requested that this process be automated using Python instead of manually with Excel. By automating this election analysis process, the hope was to use the created Python code for multiple different elections in the United States. 
## Election Audit Results
Please refer to https://github.com/tommy-chin/Election_Analysis/blob/main/PyPoll_Challenge.py for more insight on the script written for this election audit analysis and to https://github.com/tommy-chin/Election_Analysis/blob/main/analysis/election_analysis.txt for a overview of the election audit results.
### List of Questions and Answers
* How many votes were cast in this congressional election?
  * A total number of 369,711 votes were cast in this congressional election.
* Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
  * Jefferson
    * 38,885 votes and 10.5% of the total vote
  * Denver
    * 306,055 votes and 82.8% of the total vote
  * Arapahoe
    * 24,801 votes and 6.7% of the total vote
* Which county had the largest number of votes?
  * Denver county had the largest number of votes with 306,055 votes. 
* Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
  * Charles Casper Stockham
    * 85,213 votes and 23.0% of the total vote
  * Diana DeGette
    * 272,892 votes and 73.8% of the total vote
  * Raymon Anthony Doane
    * 11,606 votes and 3.1% of the total vote
* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
  * The victor of the election was Diana DeGette with a total vote count of 272,892 which was 73.8% of the total vote.
## Election Audit Summary
The Python script that was created for requested election analysis can actually be very versatile in that not much of the code needs to be altered in order to do anaylsis on other elections. If the election analysis was needed to be performed on a larger scale such as states instead of counties, any variables in the code that contain "county" would just have be changed into "states". Another issue that could happen is if the csv voting data provided had the headers in a different order. The csv voting data provided for this analysis was in the order of "Ballot ID", "County", and "Candidate". If for instance "County" and "Candidate" were swapped in another csv voting data, lines 49 and lines 52 in the Python code would need to be adjusted so that the code would pull data from the proper row of the csv. 
