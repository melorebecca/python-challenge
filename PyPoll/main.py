import os
import csv

#file path
csvpath = os.path.join('..','PyPoll','Resources', 'election_data.csv')

#define
def Poll(data):

        #variables
        total_votes = 0
        vote_count = []
        vote_percent []
        canidate_list = []
        unique_canidate = []
        winner = []

        #loop
        for row in data:

                #sum of votes
                total_votes += 1

                #append canidate names
                if row[2] not in unique_canidate:
                        unique_canidate.append(row[2])
                
                #new list
                votes.append(row[2])








# read the csv
with open(csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        csvheader = next(csvreader)
