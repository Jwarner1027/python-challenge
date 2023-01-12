import os
import csv

#Import CSV
election_csv = "/Users/jessicawarner/Desktop/python-challenge/PyPoll/resources/election_data.csv"


with open(election_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    next(csv_reader, None)

    #Define variables and empty lists
    total_votes = 0
    candidate_list = []
    candidate_col = []

    #Loop through rows in csv
    for row in csv_reader:
        candidate_col.append(str(row[2]))
        #Calculate total number of votes cast
        total_votes += 1

    #Create list of candidates who recieved votes
    for candidate in candidate_col:
        if candidate not in candidate_list:
            candidate_list.append(candidate)

    #Calculate total votes for each candidate
    vote_count = []
    for i in range(len(candidate_list)):
        candidate_name = candidate_list[i]
        vote_count.append(candidate_col.count(candidate_name))

    #Calculate percentage of votes each candidate won
    vote_percent = []
    for j in range(len(vote_count)):
        vote_percent.append((vote_count[j]/total_votes)*100)

    vote_prcnt = [ '%.3f' % elem for elem in vote_percent ]

    #Identify winner of the election based on popular vote
    win_percent_indx=vote_percent.index(max(vote_percent))
    winner=candidate_list[win_percent_indx]

print("Election Results\n")
print("---------------------------")
print("Total Votes: %d" %total_votes)
print("---------------------------")
print(str(candidate_list[0]) + ": " + str(vote_prcnt[0]) + "% (" + str(vote_count[0]) + ")")
print(str(candidate_list[1]) + ": " + str(vote_prcnt[1]) + "% (" + str(vote_count[1]) + ")")
print(str(candidate_list[2]) + ": " + str(vote_prcnt[2]) + "% (" + str(vote_count[2]) + ")")
print("---------------------------")
print("Winner: " + str(winner) + "\n")
print("---------------------------")

analysis = open('analysis.txt', 'w')

analysis.write("Election Results\n")
analysis.write("---------------------------\n")
analysis.write("Total Votes: %d\n" %total_votes)
analysis.write("---------------------------\n")
analysis.write(str(candidate_list[0]) + ": " + str(vote_prcnt[0]) + "% (" + str(vote_count[0]) + ")\n")
analysis.write(str(candidate_list[1]) + ": " + str(vote_prcnt[1]) + "% (" + str(vote_count[1]) + ")\n")
analysis.write(str(candidate_list[2]) + ": " + str(vote_prcnt[2]) + "% (" + str(vote_count[2]) + ")\n")
analysis.write("---------------------------\n")
analysis.write("Winner: " + str(winner) + "\n")
analysis.write("---------------------------")